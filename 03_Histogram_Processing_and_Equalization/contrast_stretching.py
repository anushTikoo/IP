import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

img = cv2.imread("source.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
    img = np.random.randint(50, 180, (128, 128), dtype=np.uint8)
# ----

def contrast_stretch(image):
    min_val, max_val = np.min(image), np.max(image)
    return (((image - min_val) / (max_val - min_val)) * 255).astype(np.uint8)
# ----

stretched = contrast_stretch(img)

plt.figure(figsize=(10, 4))
plt.subplot(121); plt.imshow(img, cmap='gray'); plt.title(f"Original (min={img.min()}, max={img.max()})"); plt.axis('off')
plt.subplot(122); plt.imshow(stretched, cmap='gray'); plt.title(f"Contrast Stretched (min={stretched.min()}, max={stretched.max()})"); plt.axis('off')
plt.tight_layout()
plt.show()
# ----
