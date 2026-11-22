import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

img = cv2.imread("image3.png", cv2.IMREAD_GRAYSCALE)
if img is None:
    img = np.zeros((128, 128), dtype=np.uint8)
    img[32:96, 32:96] = 200
# ----

def sobel_segmentation(image, threshold=100):
    kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    ky = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    h, w = image.shape
    grad = np.zeros((h, w), dtype=np.float32)
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            region = image[i - 1:i + 2, j - 1:j + 2]
            gx = np.sum(region * kx)
            gy = np.sum(region * ky)
            grad[i, j] = np.sqrt(gx**2 + gy**2)
    segmented = (grad > threshold).astype(np.uint8) * 255
    return grad, segmented
# ----

grad, segmented = sobel_segmentation(img)

plt.figure(figsize=(10, 4))\nplt.subplot(131); plt.imshow(img, cmap=\"gray\"); plt.title(\"Original\"); plt.axis(\"off\")\nplt.subplot(132); plt.imshow(grad, cmap=\"gray\"); plt.title(\"Sobel Gradient\"); plt.axis(\"off\")\nplt.subplot(133); plt.imshow(segmented, cmap=\"gray\"); plt.title(\"Edge-Based Segmentation\"); plt.axis(\"off\")\nplt.tight_layout()\nplt.show()\n# ----\n