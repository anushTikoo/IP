import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

sp_img = cv2.imread("salt_pepper_noise_img.png", cv2.IMREAD_GRAYSCALE)

plt.imshow(sp_img, cmap="gray")
plt.title("Salt-and-Pepper Noisy Image")
plt.axis("off")
plt.show()
# ----

rows, cols = sp_img.shape

median_img = np.zeros((rows, cols), dtype=np.uint8)

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        window = []
        for m in range(-1, 2):
            for n in range(-1, 2):
                pixel = int(sp_img[i + m][j + n])
                window.append(pixel)
        for x in range(8):
            for y in range(8 - x):
                if window[y] > window[y + 1]:
                    temp = window[y]
                    window[y] = window[y + 1]
                    window[y + 1] = temp
        median_img[i][j] = window[4]

plt.figure(figsize=(8, 4))
plt.subplot(121)
plt.imshow(sp_img, cmap="gray")
plt.title("Salt-and-Pepper Noisy Image")
plt.axis("off")

plt.subplot(122)
plt.imshow(median_img, cmap="gray")
plt.title("Median Filter Output")
plt.axis("off")

plt.tight_layout()
plt.show()
# ----
