import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

img = cv2.imread("image1.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
    img = np.zeros((128, 128), dtype=np.uint8)
    img[32:96, 32:96] = 255
# ----

def prewitt_edge_detection(image):
    kx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
    ky = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)
    h, w = image.shape
    gx = np.zeros((h, w), dtype=np.float32)
    gy = np.zeros((h, w), dtype=np.float32)
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            region = image[i - 1:i + 2, j - 1:j + 2]
            gx[i, j] = np.sum(region * kx)
            gy[i, j] = np.sum(region * ky)
    edge = np.sqrt(gx**2 + gy**2)
    return ((edge / edge.max()) * 255).astype(np.uint8) if edge.max() > 0 else edge.astype(np.uint8)
# ----

edges = prewitt_edge_detection(img)

plt.figure(figsize=(8, 4))
plt.subplot(121); plt.imshow(img, cmap="gray"); plt.title("Original"); plt.axis("off")
plt.subplot(122); plt.imshow(edges, cmap="gray"); plt.title("Prewitt Edges"); plt.axis("off")
plt.tight_layout()
plt.show()
# ----
