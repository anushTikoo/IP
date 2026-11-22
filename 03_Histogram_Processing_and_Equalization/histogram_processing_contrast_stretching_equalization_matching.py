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

def contrast_stretch(image):
    minimum = np.min(image)
    maximum = np.max(image)
    rows, cols = image.shape
    output = np.zeros_like(image)
    for i in range(rows):
        for j in range(cols):
            output[i, j] = int(((image[i, j] - minimum) / (maximum - minimum)) * 255)
    return output
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

contrast = contrast_stretch(source)
equalized = histogram_equalization(source)
matched = histogram_matching(source, target)
# ----

plt.figure(figsize=(14, 8))

plt.subplot(2, 3, 1)
plt.imshow(source, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(contrast, cmap='gray')
plt.title("Contrast Stretching")
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(equalized, cmap='gray')
plt.title("Histogram Equalization")
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(target, cmap='gray')
plt.title("Target Image")
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(matched, cmap='gray')
plt.title("Histogram Matching")
plt.axis('off')

plt.tight_layout()
plt.show()
# ----

images = [source, contrast, equalized, target, matched]
titles = [
    "Original",
    "Contrast Stretching",
    "Histogram Equalization",
    "Target",
    "Histogram Matching"
]

plt.figure(figsize=(14, 8))
for i in range(len(images)):
    plt.subplot(2, 3, i + 1)
    plt.hist(images[i].ravel(), bins=256, range=[0, 256], color='black')
    plt.title(titles[i])

plt.tight_layout()
plt.show()
# ----
