import cv2
import numpy as np
import matplotlib.pyplot as plt
# ----

image1_path = "image1.jpg"
image2_path = "image2.jpg"
image3_path = "image3.jpg"

image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
image3 = cv2.imread(image3_path, cv2.IMREAD_GRAYSCALE)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(image1, cmap="gray")
plt.title("Input Image 1")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(image2, cmap="gray")
plt.title("Input Image 2")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(image3, cmap="gray")
plt.title("Input Image 3")
plt.axis("off")

plt.tight_layout()
plt.show()
# ----

def laplacian_edge_detection(image):
    laplacian_kernel = np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
    ], dtype=np.float32)

    edge = np.zeros_like(image, dtype=np.float32)

    edge[1:-1, 1:-1] = (\n        image[:-2, :-2] * laplacian_kernel[0, 0] +\n        image[:-2, 1:-1] * laplacian_kernel[0, 1] +\n        image[:-2, 2:] * laplacian_kernel[0, 2] +\n        image[1:-1, :-2] * laplacian_kernel[1, 0] +\n        image[1:-1, 1:-1] * laplacian_kernel[1, 1] +\n        image[1:-1, 2:] * laplacian_kernel[1, 2] +\n        image[2:, :-2] * laplacian_kernel[2, 0] +\n        image[2:, 1:-1] * laplacian_kernel[2, 1] +\n        image[2:, 2:] * laplacian_kernel[2, 2]\n    )

    edge = np.abs(edge)

    maximum = np.max(edge)
    if maximum != 0:
        edge = (edge / maximum) * 255

    return edge.astype(np.uint8)

laplacian_image1 = laplacian_edge_detection(image1)
laplacian_image2 = laplacian_edge_detection(image2)
laplacian_image3 = laplacian_edge_detection(image3)
# ----

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(laplacian_image1, cmap="gray")
plt.title("Laplacian - Image 1")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(laplacian_image2, cmap="gray")
plt.title("Laplacian - Image 2")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(laplacian_image3, cmap="gray")
plt.title("Laplacian - Image 3")
plt.axis("off")

plt.tight_layout()
plt.show()
# ----
