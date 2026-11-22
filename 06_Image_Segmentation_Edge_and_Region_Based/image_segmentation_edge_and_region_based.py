import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

img = cv2.imread("image3.png", cv2.IMREAD_GRAYSCALE)
if img is None:
    img = np.zeros((128, 128), dtype=np.uint8)
    img[32:96, 32:96] = 180
# ----

# 1. Edge-Based Segmentation
kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
ky = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
h, w = img.shape
grad = np.zeros((h, w), dtype=np.float32)
for i in range(1, h - 1):
    for j in range(1, w - 1):
        r = img[i - 1:i + 2, j - 1:j + 2]
        grad[i, j] = np.sqrt(np.sum(r * kx)**2 + np.sum(r * ky)**2)
edge_seg = (grad > 80).astype(np.uint8) * 255

# 2. Region-Based Segmentation (Region Growing)
visited = np.zeros((h, w), dtype=bool)
region_seg = np.zeros((h, w), dtype=np.uint8)
seed = (h // 2, w // 2)
queue = [seed]
visited[seed] = True
region_seg[seed] = 255
r_sum, count = float(img[seed]), 1

while queue:
    x, y = queue.pop(0)
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and not visited[nx, ny]:
            visited[nx, ny] = True
            if abs(float(img[nx, ny]) - (r_sum / count)) <= 20:
                region_seg[nx, ny] = 255
                r_sum += img[nx, ny]
                count += 1
                queue.append((nx, ny))
# ----

plt.figure(figsize=(10, 4))\nplt.subplot(131); plt.imshow(img, cmap=\"gray\"); plt.title(\"Original\"); plt.axis(\"off\")\nplt.subplot(132); plt.imshow(edge_seg, cmap=\"gray\"); plt.title(\"Edge-Based\"); plt.axis(\"off\")\nplt.subplot(133); plt.imshow(region_seg, cmap=\"gray\"); plt.title(\"Region-Based\"); plt.axis(\"off\")\nplt.tight_layout()\nplt.show()\n# ----\n