import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

img = cv2.imread('images/panda.jpeg')
if img is None:
    img = np.full((256, 256, 3), 180, dtype=np.uint8)
    cv2.circle(img, (128, 128), 60, (50, 50, 50), -1)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# ----

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_img = 255 - img_rgb
# ----

plt.figure(figsize=(10, 4))
plt.subplot(131); plt.imshow(img_rgb); plt.title("Original RGB"); plt.axis('off')
plt.subplot(132); plt.imshow(gray_img, cmap='gray'); plt.title("Grayscale"); plt.axis('off')
plt.subplot(133); plt.imshow(inverted_img); plt.title("Inverted"); plt.axis('off')
plt.tight_layout()
plt.show()
# ----
