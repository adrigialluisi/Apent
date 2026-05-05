import cv2
import numpy as np
from rembg import remove
import os

images = [
    ("team-photos/Felipe.jpeg", "team-photos/Felipe_Guinle_edited.png"),
    ("team-photos/Danilo.jpeg", "team-photos/Danilo_edited.png"),
    ("team-photos/Vini.jpeg", "team-photos/Vinicius_edited.png")
]

for input_path, output_path in images:
    print(f"--- Processing {input_path} ---")
    img = cv2.imread(input_path)
    if img is None:
        continue

    print("Removing background...")
    with open(input_path, 'rb') as i:
        subject_bytes = remove(i.read())

    nparr = np.frombuffer(subject_bytes, np.uint8)
    subject = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED) # BGRA

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    h, w = subject.shape[:2]
    
    if len(faces) == 0:
        face_bottom = int(h * 0.3)
        face_center_x = w // 2
        face_top = int(h * 0.1)
        face_width = int(w * 0.3)
    else:
        faces = sorted(faces, key=lambda f: f[2]*f[3], reverse=True)
        x, y, w_f, h_f = faces[0]
        face_bottom = y + h_f
        face_center_x = x + w_f // 2
        face_top = y
        face_width = w_f

    bgr = subject[:, :, :3].astype(np.float32)
    alpha = subject[:, :, 3].astype(np.float32) / 255.0

    target_w, target_h = 800, 800
    target_face_width = target_w * 0.38 
    scale = target_face_width / float(face_width)

    # Gentle fade towards the bottom and sides
    rows_with_alpha = np.where(alpha > 0)[0]
    subject_bottom = rows_with_alpha[-1] if len(rows_with_alpha) > 0 else h

    # Fade out naturally towards whatever the subject_bottom is
    fade_start = face_bottom + int(face_width * 0.2)
    fade_end = subject_bottom

    alpha_gradient = np.ones((h, w), dtype=np.float32)
    for y_idx in range(h):
        if y_idx > fade_start:
            if y_idx > fade_end:
                alpha_gradient[y_idx, :] = 0.0
            else:
                t = (y_idx - fade_start) / float(fade_end - fade_start + 1e-5)
                val = np.cos(t * np.pi / 2.0)
                alpha_gradient[y_idx, :] = max(0.0, val)

    cols_with_alpha = np.where(np.max(alpha, axis=0) > 0)[0]
    if len(cols_with_alpha) > 0:
        subject_left = cols_with_alpha[0]
        subject_right = cols_with_alpha[-1]
        side_fade_dist = int(face_width * 0.4)
        for x_idx in range(w):
            if x_idx < subject_left + side_fade_dist:
                t = (subject_left + side_fade_dist - x_idx) / float(side_fade_dist)
                val = np.cos(t * np.pi / 2.0)
                alpha_gradient[:, x_idx] *= max(0.0, val)
            elif x_idx > subject_right - side_fade_dist:
                t = (x_idx - (subject_right - side_fade_dist)) / float(side_fade_dist)
                val = np.cos(t * np.pi / 2.0)
                alpha_gradient[:, x_idx] *= max(0.0, val)

    final_alpha = alpha * alpha_gradient

    # BGR for #1e2630 (Card Background)
    bg_color = np.array([48, 38, 30], dtype=np.float32) 

    final_alpha_3d = np.expand_dims(final_alpha, axis=2)
    composed = bgr * final_alpha_3d + bg_color * (1.0 - final_alpha_3d)
    composed = np.clip(composed, 0, 255).astype(np.uint8)

    new_w = int(w * scale)
    new_h = int(h * scale)
    composed_scaled = cv2.resize(composed, (new_w, new_h), interpolation=cv2.INTER_AREA)

    new_face_center_x = int(face_center_x * scale)
    new_face_top = int(face_top * scale)
    new_face_bottom = int(face_bottom * scale)

    canvas = np.full((target_h, target_w, 3), bg_color, dtype=np.uint8)

    face_center_y = (new_face_top + new_face_bottom) // 2
    paste_x = target_w // 2 - new_face_center_x
    paste_y = int(target_h * 0.35) - face_center_y

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
