import numpy as np
import matplotlib.pyplot as plt
# ----

img = np.zeros((100, 100), dtype=np.uint8)
img[25:75, 25:75] = 1
img[40:60, 40:60] = 0
kernel = np.ones((3, 3), dtype=np.uint8)

def erosion(image, kernel):
    pad = kernel.shape[0] // 2
    padded = np.pad(image, pad)
    h, w = image.shape
    out = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if np.all(padded[i:i + kernel.shape[0], j:j + kernel.shape[1]][kernel == 1] == 1):
                out[i, j] = 1
    return out

def dilation(image, kernel):
    pad = kernel.shape[0] // 2
    padded = np.pad(image, pad)
    h, w = image.shape
    out = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if np.any(padded[i:i + kernel.shape[0], j:j + kernel.shape[1]][kernel == 1] == 1):
                out[i, j] = 1
    return out
# ----

eroded = erosion(img, kernel)
dilated = dilation(img, kernel)
opening = dilation(erosion(img, kernel), kernel)
closing = erosion(dilation(img, kernel), kernel)
boundary = img - eroded
# ----

results = [("Original", img), ("Erosion", eroded), ("Dilation", dilated),
           ("Opening", opening), ("Closing", closing), ("Boundary", boundary)]

plt.figure(figsize=(14, 6))\nfor i, (title, out) in enumerate(results):\n    plt.subplot(2, 3, i + 1)\n    plt.imshow(out, cmap=\"gray\")\n    plt.title(title)\n    plt.axis(\"off\")\n\nplt.tight_layout()\nplt.show()\n# ----\n