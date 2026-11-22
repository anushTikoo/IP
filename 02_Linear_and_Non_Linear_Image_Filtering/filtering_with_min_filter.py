import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

salt_img = cv2.imread("salt_noise_img.jpg", cv2.IMREAD_GRAYSCALE)

plt.imshow(salt_img, cmap="gray")
plt.title("Salt Noise Image")
plt.axis("off")
plt.show()
# ----

rows, cols = salt_img.shape

min_img = np.zeros((rows, cols), dtype=np.uint8)

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        minimum = 255
        for m in range(-1, 2):
            for n in range(-1, 2):
                pixel = int(salt_img[i + m][j + n])
                if pixel < minimum:
                    minimum = pixel
        min_img[i][j] = minimum

plt.figure(figsize=(8, 4))
plt.subplot(121)
plt.imshow(salt_img, cmap="gray")
plt.title("Salt Noisy Image")
plt.axis("off")

plt.subplot(122)
plt.imshow(min_img, cmap="gray")
plt.title("Min Filter Output")
plt.axis("off")

plt.tight_layout()
plt.show()
# ----
