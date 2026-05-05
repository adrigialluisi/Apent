import cv2
import numpy as np

input_path = "team-photos/Felipe.png"
output_path = "team-photos/Felipe_Guinle_edited.png"

img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
if img is None:
    print(f"Error: Could not read {input_path}")
    exit(1)

h, w = img.shape[:2]
bgr = img[:, :, :3].astype(np.float32)

if img.shape[2] == 4:
    alpha = img[:, :, 3].astype(np.float32) / 255.0
else:
    alpha = np.ones((h, w), dtype=np.float32)

# Fade vertical at the bottom
fade_dist = int(h * 0.35)
fade_start = h - fade_dist

alpha_gradient = np.ones((h, w), dtype=np.float32)
for y_idx in range(h):
    if y_idx > fade_start:
        t = (y_idx - fade_start) / float(fade_dist)
        val = np.cos(t * np.pi / 2.0)
        alpha_gradient[y_idx, :] = max(0.0, val)

# Also fade the sides horizontally to ensure no harsh borders
side_fade_dist = int(w * 0.1)
for x_idx in range(w):
    if x_idx < side_fade_dist:
        t = (side_fade_dist - x_idx) / float(side_fade_dist)
        val = np.cos(t * np.pi / 2.0)
        alpha_gradient[:, x_idx] *= val
    elif x_idx > w - side_fade_dist:
        t = (x_idx - (w - side_fade_dist)) / float(side_fade_dist)
        val = np.cos(t * np.pi / 2.0)
        alpha_gradient[:, x_idx] *= val

final_alpha = alpha * alpha_gradient

# Composite on #182028
bg_color = np.array([40, 32, 24], dtype=np.float32) # BGR for #182028
final_alpha_3d = np.expand_dims(final_alpha, axis=2)
composed = bgr * final_alpha_3d + bg_color * (1.0 - final_alpha_3d)
composed = np.clip(composed, 0, 255).astype(np.uint8)

# Scale down to add more background and match the 800x1000 format
target_w, target_h = 800, 1000
scale = 0.65
new_w = int(w * scale)
new_h = int(h * scale)
composed_scaled = cv2.resize(composed, (new_w, new_h), interpolation=cv2.INTER_AREA)

canvas = np.full((target_h, target_w, 3), bg_color, dtype=np.uint8)

# We want the subject to be near the bottom, centered horizontally
paste_x = (target_w - new_w) // 2
paste_y = target_h - new_h + 30 # Push it down a bit so bottom fade meets edge

c_x1 = max(0, paste_x)
c_y1 = max(0, paste_y)
c_x2 = min(target_w, paste_x + new_w)
c_y2 = min(target_h, paste_y + new_h)

i_x1 = max(0, -paste_x)
i_y1 = max(0, -paste_y)
i_x2 = i_x1 + (c_x2 - c_x1)
i_y2 = i_y1 + (c_y2 - c_y1)

if c_x2 > c_x1 and c_y2 > c_y1:
    canvas[c_y1:c_y2, c_x1:c_x2] = composed_scaled[i_y1:i_y2, i_x1:i_x2]

cv2.imwrite(output_path, canvas)
print(f"Done! Saved to {output_path}")
