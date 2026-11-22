import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

img = cv2.imread("source.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
    img = np.random.randint(50, 180, (128, 128), dtype=np.uint8)
# ----

def compute_histogram(image):
    hist = np.zeros(256, dtype=int)
    for pixel in image.ravel():
        hist[pixel] += 1
    return hist

def histogram_equalization(image):
    hist = compute_histogram(image)
    cdf = hist.cumsum()
    lookup = (cdf / cdf[-1] * 255).astype(np.uint8)
    return lookup[image]
# ----

equalized = histogram_equalization(img)

plt.figure(figsize=(10, 6))
plt.subplot(221); plt.imshow(img, cmap='gray'); plt.title("Original"); plt.axis('off')
plt.subplot(222); plt.imshow(equalized, cmap='gray'); plt.title("Equalized"); plt.axis('off')
plt.subplot(223); plt.plot(compute_histogram(img)); plt.title("Original Histogram")
plt.subplot(224); plt.plot(compute_histogram(equalized)); plt.title("Equalized Histogram")
plt.tight_layout()\nplt.show()\n# ----\n