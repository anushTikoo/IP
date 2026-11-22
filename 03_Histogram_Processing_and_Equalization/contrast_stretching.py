import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

source = cv2.imread("source.jpg", 0)
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

contrast = contrast_stretch(source)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(source, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(contrast, cmap='gray')
plt.title("Contrast Stretching")
plt.axis('off')
plt.tight_layout()
plt.show()
# ----
