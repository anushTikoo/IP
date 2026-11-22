import numpy as np
import matplotlib.pyplot as plt
# ----

img = np.zeros((100, 100), dtype=np.uint8)
img[10:30, 10:30] = 1
img[50:90, 50:90] = 1
img[70:73, 10:13] = 1  # small object
# ----

def connected_components(image):
    h, w = image.shape
    labels = np.zeros((h, w), dtype=int)
    current_label = 0
    components = {}

    for i in range(h):
        for j in range(w):
            if image[i, j] == 1 and labels[i, j] == 0:
                current_label += 1
                queue = [(i, j)]
                labels[i, j] = current_label
                pixels = []

                while queue:
                    ci, cj = queue.pop(0)
                    pixels.append((ci, cj))
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < h and 0 <= nj < w and image[ni, nj] == 1 and labels[ni, nj] == 0:
                            labels[ni, nj] = current_label
                            queue.append((ni, nj))
                components[current_label] = pixels
    return labels, components

labels, components = connected_components(img)
cleaned = np.zeros_like(img)
for label, pixels in components.items():
    if len(pixels) >= 20:  # remove small objects
        for r, c in pixels:
            cleaned[r, c] = 1
# ----

plt.figure(figsize=(9, 3))
plt.subplot(131); plt.imshow(img, cmap="gray"); plt.title("Original"); plt.axis("off")
plt.subplot(132); plt.imshow(labels, cmap="nipy_spectral"); plt.title("Labeled Components"); plt.axis("off")
plt.subplot(133); plt.imshow(cleaned, cmap="gray"); plt.title("Small Objects Removed"); plt.axis("off")
plt.tight_layout()
plt.show()
# ----
