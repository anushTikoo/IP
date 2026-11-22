import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

img = cv2.imread("image1.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
    img = np.zeros((128, 128), dtype=np.uint8)
    img[32:96, 32:96] = 255

def convolve2d(image, kernel):
    h, w = image.shape
    out = np.zeros((h, w), dtype=np.float32)
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            out[i, j] = np.sum(image[i - 1:i + 2, j - 1:j + 2] * kernel)
    return out
# ----

sobel_kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_ky = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
sobel = np.sqrt(convolve2d(img, sobel_kx)**2 + convolve2d(img, sobel_ky)**2)

prewitt_kx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewitt_ky = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
prewitt = np.sqrt(convolve2d(img, prewitt_kx)**2 + convolve2d(img, prewitt_ky)**2)

laplacian_k = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
laplacian = np.abs(convolve2d(img, laplacian_k))
# ----

plt.figure(figsize=(12, 4))
plt.subplot(141); plt.imshow(img, cmap="gray"); plt.title("Original"); plt.axis("off")
plt.subplot(142); plt.imshow(sobel, cmap="gray"); plt.title("Sobel"); plt.axis("off")
plt.subplot(143); plt.imshow(prewitt, cmap="gray"); plt.title("Prewitt"); plt.axis("off")
plt.subplot(144); plt.imshow(laplacian, cmap="gray"); plt.title("Laplacian"); plt.axis("off")
plt.tight_layout()
plt.show()
# ----
