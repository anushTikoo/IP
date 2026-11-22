import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

img = cv2.imread("salt_noise_img.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
    img = np.random.randint(50, 200, (128, 128), dtype=np.uint8)

rows, cols = img.shape
min_img = np.zeros((rows, cols), dtype=np.uint8)
# ----

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        region = img[i - 1:i + 2, j - 1:j + 2]
        min_img[i, j] = np.min(region)
# ----

plt.figure(figsize=(8, 4))
plt.subplot(121); plt.imshow(img, cmap="gray"); plt.title("Salt Noise Image"); plt.axis("off")
plt.subplot(122); plt.imshow(min_img, cmap="gray"); plt.title("Min Filter Output"); plt.axis("off")
plt.tight_layout()
plt.show()
# ----
