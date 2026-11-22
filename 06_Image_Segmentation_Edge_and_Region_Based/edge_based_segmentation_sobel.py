import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
# ----

def load_grayscale(path):
    img = Image.open(path).convert('L')
    return np.array(img, dtype=np.float64)
# ----

def convolve2d(image, kernel):
    k_h, k_w = kernel.shape
    pad_h, pad_w = k_h // 2, k_w // 2
    padded = np.pad(
        image,
        ((pad_h, pad_h), (pad_w, pad_w)),
        mode='constant'
    )
    output = np.zeros_like(image)
    flipped_kernel = np.flipud(np.fliplr(kernel))
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded[i:i + k_h, j:j + k_w]
            output[i, j] = np.sum(region * flipped_kernel)
    return output
# ----

def edge_based_segmentation(image, threshold):
    sobel_x = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ], dtype=np.float64)
    sobel_y = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ], dtype=np.float64)
    grad_x = convolve2d(image, sobel_x)
    grad_y = convolve2d(image, sobel_y)
    magnitude = np.sqrt(grad_x ** 2 + grad_y ** 2)
    magnitude = (magnitude / magnitude.max()) * 255
    segmented = (magnitude > threshold).astype(np.uint8) * 255
    return magnitude, segmented
# ----

edge_configs = [
    {"path": "image1.jpg", "edge_threshold": 60},
    {"path": "image2.jpg", "edge_threshold": 60},
]

fig, axes = plt.subplots(2, 3, figsize=(14, 10))
for row, cfg in enumerate(edge_configs):
    img = load_grayscale(cfg["path"])
    magnitude, edge_segmented = edge_based_segmentation(
        img,
        cfg["edge_threshold"]
    )
    axes[row, 0].imshow(img, cmap='gray')
    axes[row, 0].set_title(f'{cfg["path"]} - Original')
    axes[row, 1].imshow(magnitude, cmap='gray')
    axes[row, 1].set_title('Sobel Gradient Magnitude')
    axes[row, 2].imshow(edge_segmented, cmap='gray')
    axes[row, 2].set_title('Edge-Based Segmentation')
    for ax in axes[row]:
        ax.axis('off')
plt.tight_layout()
plt.show()
# ----
