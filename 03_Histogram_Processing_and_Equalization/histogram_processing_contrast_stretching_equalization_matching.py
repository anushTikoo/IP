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
    for p in image.ravel():
        hist[p] += 1
    cdf = hist.cumsum()
    return cdf / cdf[-1]

stretched = (((source - source.min()) / (source.max() - source.min())) * 255).astype(np.uint8)

cdf = get_cdf(source)
equalized = (cdf[source] * 255).astype(np.uint8)

src_cdf = get_cdf(source)
tgt_cdf = get_cdf(target)
lookup = np.array([np.argmin(np.abs(src_cdf[s] - tgt_cdf)) for s in range(256)], dtype=np.uint8)
matched = lookup[source]
# ----

plt.figure(figsize=(12, 4))
plt.subplot(141); plt.imshow(source, cmap='gray'); plt.title("Original"); plt.axis('off')
plt.subplot(142); plt.imshow(stretched, cmap='gray'); plt.title("Stretched"); plt.axis('off')
plt.subplot(143); plt.imshow(equalized, cmap='gray'); plt.title("Equalized"); plt.axis('off')
plt.subplot(144); plt.imshow(matched, cmap='gray'); plt.title("Matched"); plt.axis('off')
plt.tight_layout()
plt.show()
# ----
