import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

img = cv2.imread('images/panda.jpeg')
if img is None:
    img = np.full((256, 256, 3), 180, dtype=np.uint8)
    cv2.circle(img, (128, 128), 60, (50, 50, 50), -1)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# ----

resized = cv2.resize(img_rgb, (200, 200))
rotated = cv2.rotate(img_rgb, cv2.ROTATE_90_CLOCKWISE)
flipped = cv2.flip(img_rgb, 1)
cropped = img_rgb[50:200, 50:200]
# ----

transforms = [("Original", img_rgb), ("Resized", resized), ("Rotated 90°", rotated), ("Flipped", flipped), ("Cropped", cropped)]

plt.figure(figsize=(12, 4))
for i, (title, out) in enumerate(transforms):
    plt.subplot(1, 5, i + 1)
    plt.imshow(out)
    plt.title(title)
    plt.axis('off')

plt.tight_layout()
plt.show()
# ----
