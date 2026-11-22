import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image1.png")
img = img[:1050, :]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ----

_, mask = cv2.threshold(
    gray,
    245,
    255,
    cv2.THRESH_BINARY_INV
)
kernel = np.ones((5, 5), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
contours, _ = cv2.findContours(
    mask,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
output = img.copy()
for contour in contours:
    area = cv2.contourArea(contour)
    if area < 10000:
        continue
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(
        output,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        4
    )
# ----

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(mask, cmap="gray")
plt.title("Binary Mask")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(output_rgb)
plt.title("Detected Bounding Boxes")
plt.axis("off")

plt.tight_layout()
plt.show()
# ----
