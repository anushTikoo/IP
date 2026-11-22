import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

source = cv2.imread("source.jpg", cv2.IMREAD_GRAYSCALE)
target = cv2.imread("target.jpg", cv2.IMREAD_GRAYSCALE)
if source is None:
    source = np.random.randint(40, 140, (128, 128), dtype=np.uint8)
if target is None:
    target = np.random.randint(120, 240, (128, 128), dtype=np.uint8)
# ----

def get_cdf(image):
    hist = np.zeros(256, dtype=int)
    for pixel in image.ravel():
        hist[pixel] += 1
    cdf = hist.cumsum()
    return cdf / cdf[-1]

def histogram_matching(src, tgt):
    src_cdf = get_cdf(src)
    tgt_cdf = get_cdf(tgt)
    lookup = np.zeros(256, dtype=np.uint8)
    for s in range(256):
        lookup[s] = np.argmin(np.abs(src_cdf[s] - tgt_cdf))
    return lookup[src]
# ----

matched = histogram_matching(source, target)

plt.figure(figsize=(10, 4))
plt.subplot(131); plt.imshow(source, cmap='gray'); plt.title("Source"); plt.axis('off')
plt.subplot(132); plt.imshow(target, cmap='gray'); plt.title("Target"); plt.axis('off')
plt.subplot(133); plt.imshow(matched, cmap='gray'); plt.title("Matched Output"); plt.axis('off')
plt.tight_layout()
plt.show()
# ----
