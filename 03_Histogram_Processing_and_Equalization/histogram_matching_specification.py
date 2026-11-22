import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

source = cv2.imread("source.jpg", 0)
target = cv2.imread("target.jpg", 0)
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

def histogram_matching(source, target):
    source_hist = compute_histogram(source)
    target_hist = compute_histogram(target)
    source_cdf = compute_cdf(source_hist)
    target_cdf = compute_cdf(target_hist)
    mapping = np.zeros(256, dtype=np.uint8)
    for i in range(256):
        difference = np.abs(target_cdf - source_cdf[i])
        mapping[i] = np.argmin(difference)
    rows, cols = source.shape
    output = np.zeros_like(source)
    for i in range(rows):
        for j in range(cols):
            output[i, j] = mapping[source[i, j]]
    return output
# ----

matched = histogram_matching(source, target)

plt.figure(figsize=(14, 5))
plt.subplot(1, 3, 1)
plt.imshow(source, cmap='gray')
plt.title("Source Original")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(target, cmap='gray')
plt.title("Target Reference")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(matched, cmap='gray')
plt.title("Histogram Matched")
plt.axis('off')
plt.tight_layout()
plt.show()
# ----
