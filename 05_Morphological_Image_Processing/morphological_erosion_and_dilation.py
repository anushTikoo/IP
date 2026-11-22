import numpy as np
import matplotlib.pyplot as plt
# ----

img = np.zeros((100, 100), dtype=np.uint8)
img[25:75, 25:75] = 1
img[40:60, 40:60] = 0
kernel = np.ones((3, 3), dtype=np.uint8)
# ----

def erosion(image, kernel):
    pad = kernel.shape[0] // 2
    padded = np.pad(image, pad)
    h, w = image.shape
    output = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            region = padded[i:i + kernel.shape[0], j:j + kernel.shape[1]]
            if np.all(region[kernel == 1] == 1):
                output[i, j] = 1
    return output

def dilation(image, kernel):
    pad = kernel.shape[0] // 2
    padded = np.pad(image, pad)
    h, w = image.shape
    output = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            region = padded[i:i + kernel.shape[0], j:j + kernel.shape[1]]
            if np.any(region[kernel == 1] == 1):
                output[i, j] = 1
    return output
# ----

eroded = erosion(img, kernel)
dilated = dilation(img, kernel)

plt.figure(figsize=(9, 3))
plt.subplot(131); plt.imshow(img, cmap=\"gray\"); plt.title(\"Original Binary\"); plt.axis(\"off\")
plt.subplot(132); plt.imshow(eroded, cmap=\"gray\"); plt.title(\"Erosion\"); plt.axis(\"off\")
plt.subplot(133); plt.imshow(dilated, cmap=\"gray\"); plt.title(\"Dilation\"); plt.axis(\"off\")
plt.tight_layout()
plt.show()
# ----
