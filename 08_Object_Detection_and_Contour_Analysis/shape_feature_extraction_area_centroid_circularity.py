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
    perimeter = cv2.arcLength(c, True)
    circularity = (4 * np.pi * area) / (perimeter**2) if perimeter > 0 else 0
    M = cv2.moments(c)
    cx = int(M["m10"] / M["m00"]) if M["m00"] != 0 else 0
    cy = int(M["m01"] / M["m00"]) if M["m00"] != 0 else 0

    print(f"Object {i + 1} -> Area: {area:.1f}, Perimeter: {perimeter:.1f}, Circularity: {circularity:.2f}, Centroid: ({cx}, {cy})")
    cv2.circle(output, (cx, cy), 5, (255, 0, 0), -1)
    cv2.putText(output, f"Obj {i + 1}", (cx - 20, cy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
# ----

plt.figure(figsize=(6, 6))\nplt.imshow(output)\nplt.title(\"Shape Feature Extraction (Centroids & Labels)\")\nplt.axis(\"off\")\nplt.tight_layout()\nplt.show()\n# ----\n