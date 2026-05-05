import cv2
import numpy as np
from rembg import remove

images = ["team-photos/Felipe.jpeg", "team-photos/Danilo.jpeg", "team-photos/Vini.jpeg"]
for path in images:
    with open(path, 'rb') as i:
        subject_bytes = remove(i.read())
    nparr = np.frombuffer(subject_bytes, np.uint8)
    subject = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
    gray = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = sorted(face_cascade.detectMultiScale(gray, 1.1, 4), key=lambda f: f[2]*f[3], reverse=True)
    if faces:
        x, y, w, h = faces[0]
        face_bottom = y + h
        face_width = w
        alpha = subject[:, :, 3]
        rows = np.where(alpha > 0)[0]
        sub_bottom = rows[-1] if len(rows) > 0 else subject.shape[0]
        ratio = (sub_bottom - face_bottom) / face_width
        print(f"{path}: face_width={face_width}, face_bottom={face_bottom}, subject_bottom={sub_bottom}, body_visible_ratio={ratio:.2f}")
