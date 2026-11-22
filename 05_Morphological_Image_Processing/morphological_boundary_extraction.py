import numpy as np
import matplotlib.pyplot as plt
# ----

img = np.zeros((100, 100), dtype=np.uint8)
img[25:75, 25:75] = 1
kernel = np.ones((3, 3), dtype=np.uint8)

def erosion(image, kernel):
    pad = kernel.shape[0] // 2
    padded = np.pad(image, pad)
    h, w = image.shape
    output = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if np.all(padded[i:i + kernel.shape[0], j:j + kernel.shape[1]][kernel == 1] == 1):
                output[i, j] = 1
    return output
# ----

boundary = img - erosion(img, kernel)
# ----

plt.figure(figsize=(8, 4))
plt.subplot(121); plt.imshow(img, cmap="gray"); plt.title("Original Object"); plt.axis("off")
plt.subplot(122); plt.imshow(boundary, cmap="gray"); plt.title("Extracted Boundary"); plt.axis("off")
plt.tight_layout()
plt.show()
# ----
