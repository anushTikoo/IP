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
_, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# ----

output = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
for i, c in enumerate(contours):
    area = cv2.contourArea(c)
    if area < 500:
        continue
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
    M = cv2.moments(c)
    if M["m00"] != 0:
        cx, cy = int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])
        cv2.circle(output, (cx, cy), 4, (255, 0, 0), -1)
# ----

plt.figure(figsize=(10, 5))\nplt.subplot(121); plt.imshow(mask, cmap=\"gray\"); plt.title(\"Thresholded Mask\"); plt.axis(\"off\")\nplt.subplot(122); plt.imshow(output); plt.title(\"Object Detection & Contours\"); plt.axis(\"off\")\nplt.tight_layout()\nplt.show()\n# ----\n