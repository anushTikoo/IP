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

def prewitt_edge_detection(image):
    prewitt_x = np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ], dtype=np.float32)

    prewitt_y = np.array([
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1]
    ], dtype=np.float32)

    gx = np.zeros_like(image, dtype=np.float32)
    gy = np.zeros_like(image, dtype=np.float32)

    gx[1:-1, 1:-1] = (
        image[:-2, :-2] * prewitt_x[0, 0] +
        image[:-2, 1:-1] * prewitt_x[0, 1] +
        image[:-2, 2:] * prewitt_x[0, 2] +
        image[1:-1, :-2] * prewitt_x[1, 0] +
        image[1:-1, 1:-1] * prewitt_x[1, 1] +
        image[1:-1, 2:] * prewitt_x[1, 2] +
        image[2:, :-2] * prewitt_x[2, 0] +
        image[2:, 1:-1] * prewitt_x[2, 1] +
        image[2:, 2:] * prewitt_x[2, 2]
    )

    gy[1:-1, 1:-1] = (
        image[:-2, :-2] * prewitt_y[0, 0] +
        image[:-2, 1:-1] * prewitt_y[0, 1] +
        image[:-2, 2:] * prewitt_y[0, 2] +
        image[1:-1, :-2] * prewitt_y[1, 0] +
        image[1:-1, 1:-1] * prewitt_y[1, 1] +
        image[1:-1, 2:] * prewitt_y[1, 2] +
        image[2:, :-2] * prewitt_y[2, 0] +
        image[2:, 1:-1] * prewitt_y[2, 1] +
        image[2:, 2:] * prewitt_y[2, 2]
    )

    edge = np.sqrt(gx**2 + gy**2)

    maximum = np.max(edge)
    if maximum != 0:
        edge = (edge / maximum) * 255

    return edge.astype(np.uint8)

prewitt_image1 = prewitt_edge_detection(image1)
prewitt_image2 = prewitt_edge_detection(image2)
prewitt_image3 = prewitt_edge_detection(image3)
# ----

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(prewitt_image1, cmap="gray")
plt.title("Prewitt - Image 1")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(prewitt_image2, cmap="gray")
plt.title("Prewitt - Image 2")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(prewitt_image3, cmap="gray")
plt.title("Prewitt - Image 3")
plt.axis("off")

plt.tight_layout()
plt.show()
# ----
