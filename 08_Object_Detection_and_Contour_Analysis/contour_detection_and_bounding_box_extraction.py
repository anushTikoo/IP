import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

img = cv2.imread("image1.png")
if img is None:
    img = np.full((300, 300, 3), 255, dtype=np.uint8)
    cv2.circle(img, (80, 80), 40, (0, 0, 0), -1)
    cv2.rectangle(img, (180, 150), (260, 250), (0, 0, 0), -1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ----

_, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

output = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
for c in contours:
    if cv2.contourArea(c) > 500:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 3)
# ----

plt.figure(figsize=(8, 4))\nplt.subplot(121); plt.imshow(mask, cmap=\"gray\"); plt.title(\"Binary Mask\"); plt.axis(\"off\")\nplt.subplot(122); plt.imshow(output); plt.title(\"Detected Bounding Boxes\"); plt.axis(\"off\")\nplt.tight_layout()\nplt.show()\n# ----\n