import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

img = cv2.imread("gaussian_noise_img.png", cv2.IMREAD_GRAYSCALE)
if img is None:
    img = np.random.randint(50, 200, (128, 128), dtype=np.uint8)

rows, cols = img.shape
mean_out = np.zeros((rows, cols), dtype=np.uint8)
median_out = np.zeros((rows, cols), dtype=np.uint8)
min_out = np.zeros((rows, cols), dtype=np.uint8)
# ----

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        region = img[i - 1:i + 2, j - 1:j + 2]
        mean_out[i, j] = int(np.sum(region) // 9)
        median_out[i, j] = int(np.median(region))
        min_out[i, j] = np.min(region)
# ----

plt.figure(figsize=(12, 4))
plt.subplot(141); plt.imshow(img, cmap="gray"); plt.title("Original Noisy"); plt.axis("off")
plt.subplot(142); plt.imshow(mean_out, cmap="gray"); plt.title("Mean Filter"); plt.axis("off")
plt.subplot(143); plt.imshow(median_out, cmap="gray"); plt.title("Median Filter"); plt.axis("off")
plt.subplot(144); plt.imshow(min_out, cmap="gray"); plt.title("Min Filter"); plt.axis("off")
plt.tight_layout()
plt.show()
# ----
