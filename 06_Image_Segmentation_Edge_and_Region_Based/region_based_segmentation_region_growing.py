import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

img = cv2.imread("image3.png", cv2.IMREAD_GRAYSCALE)
if img is None:
    img = np.zeros((128, 128), dtype=np.uint8)
    img[32:96, 32:96] = 180
# ----

def region_growing(image, seed, threshold=15):
    h, w = image.shape
    visited = np.zeros((h, w), dtype=bool)
    mask = np.zeros((h, w), dtype=np.uint8)
    queue = [seed]
    visited[seed] = True
    mask[seed] = 255
    region_sum = float(image[seed])
    count = 1

    while queue:
        x, y = queue.pop(0)
        mean_val = region_sum / count
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx, ny]:
                visited[nx, ny] = True
                if abs(float(image[nx, ny]) - mean_val) <= threshold:
                    mask[nx, ny] = 255
                    region_sum += image[nx, ny]
                    count += 1
                    queue.append((nx, ny))
    return mask
# ----

mask = region_growing(img, seed=(64, 64), threshold=20)

plt.figure(figsize=(8, 4))
plt.subplot(121); plt.imshow(img, cmap=\"gray\"); plt.title(\"Original\"); plt.axis(\"off\")
plt.subplot(122); plt.imshow(mask, cmap=\"gray\"); plt.title(\"Region Growing Segmentation\"); plt.axis(\"off\")
plt.tight_layout()
plt.show()
# ----
