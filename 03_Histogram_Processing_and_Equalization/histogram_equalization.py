import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

source = cv2.imread("source.jpg", 0)
# ----

def compute_histogram(image):
    histogram = np.zeros(256, dtype=int)
    rows, cols = image.shape
    for i in range(rows):
        for j in range(cols):
            histogram[image[i, j]] += 1
    return histogram
# ----

def compute_cdf(histogram):
    cdf = np.zeros(256)
    cdf[0] = histogram[0]
    for i in range(1, 256):
        cdf[i] = cdf[i-1] + histogram[i]
    cdf = cdf / cdf[-1]
    return cdf
# ----

def histogram_equalization(image):
    histogram = compute_histogram(image)
    cdf = compute_cdf(histogram)
    lookup = np.zeros(256, dtype=np.uint8)
    for i in range(256):
        lookup[i] = int(cdf[i] * 255)
    rows, cols = image.shape
    output = np.zeros_like(image)
    for i in range(rows):
        for j in range(cols):
            output[i, j] = lookup[image[i, j]]
    return output
# ----

equalized = histogram_equalization(source)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(source, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(equalized, cmap='gray')
plt.title("Histogram Equalization")
plt.axis('off')
plt.tight_layout()
plt.show()
# ----
