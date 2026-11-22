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
object_count = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if area < 10000:
        continue
    object_count += 1
    x, y, w, h = cv2.boundingRect(contour)
    moments = cv2.moments(contour)
    if moments["m00"] != 0:
        cx = int(moments["m10"] / moments["m00"])
        cy = int(moments["m01"] / moments["m00"])
    else:
        cx = x + w // 2
        cy = y + h // 2
    perimeter = cv2.arcLength(contour, True)
    if perimeter != 0:
        circularity = (4 * np.pi * area) / (perimeter ** 2)
    else:
        circularity = 0
    print("--------------------------------")
    print("Object:", object_count)
    print("Area:", round(area, 2))
    print("Centroid:", (cx, cy))
    print("Circularity:", round(circularity, 3))
    cv2.circle(
        output,
        (cx, cy),
        7,
        (0, 0, 255),
        -1
    )
    cv2.putText(
        output,
        f"Object {object_count}",
        (x, y - 15),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        3
    )

print("\n==============================")
print("TOTAL OBJECTS:", object_count)
print("==============================")
# ----

output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8, 8))
plt.imshow(output_rgb)
plt.title(f"Centroids and Labels (Objects: {object_count})")
plt.axis("off")
plt.tight_layout()
plt.show()
# ----
