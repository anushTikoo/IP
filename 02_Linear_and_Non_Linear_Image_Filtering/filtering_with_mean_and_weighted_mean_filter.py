import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

gaussian_img = cv2.imread("gaussian_noise_img.png", cv2.IMREAD_GRAYSCALE)

plt.imshow(gaussian_img, cmap="gray")
plt.title("Gaussian Noisy Image")
plt.axis("off")
plt.show()
# ----

rows, cols = gaussian_img.shape

mean_img = np.zeros((rows, cols), dtype=np.uint8)
weighted_img = np.zeros((rows, cols), dtype=np.uint8)

kernel = [
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
]

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        total = 0
        weighted_sum = 0
        for m in range(-1, 2):
            for n in range(-1, 2):
                pixel = int(gaussian_img[i + m][j + n])
                total += pixel
                weighted_sum += pixel * kernel[m + 1][n + 1]
        mean_img[i][j] = total // 9
        weighted_img[i][j] = weighted_sum // 16

plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(gaussian_img, cmap="gray")
plt.title("Gaussian Noisy Image")
plt.axis("off")

plt.subplot(132)
plt.imshow(mean_img, cmap="gray")
plt.title("Mean Filter Output")
plt.axis("off")

plt.subplot(133)
plt.imshow(weighted_img, cmap="gray")
plt.title("Weighted Mean Output")
plt.axis("off")

plt.tight_layout()
plt.show()
# ----
