import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

img = cv2.imread("gaussian_noise_img.png", cv2.IMREAD_GRAYSCALE)
if img is None:
    img = np.random.randint(50, 200, (128, 128), dtype=np.uint8)

rows, cols = img.shape
mean_img = np.zeros((rows, cols), dtype=np.uint8)
weighted_img = np.zeros((rows, cols), dtype=np.uint8)

w_kernel = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
])
# ----

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        region = img[i - 1:i + 2, j - 1:j + 2]
        mean_img[i, j] = int(np.sum(region) // 9)
        weighted_img[i, j] = int(np.sum(region * w_kernel) // 16)
# ----

plt.figure(figsize=(10, 4))
plt.subplot(131); plt.imshow(img, cmap="gray"); plt.title("Gaussian Noisy Image"); plt.axis("off")
plt.subplot(132); plt.imshow(mean_img, cmap="gray"); plt.title("Mean Filter (3x3)"); plt.axis("off")
plt.subplot(133); plt.imshow(weighted_img, cmap="gray"); plt.title("Weighted Mean Filter"); plt.axis("off")
plt.tight_layout()
plt.show()
# ----
