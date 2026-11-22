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

def region_growing(image, seed, threshold):
    h, w = image.shape
    visited = np.zeros((h, w), dtype=bool)
    mask = np.zeros((h, w), dtype=np.uint8)
    seed_x, seed_y = seed
    region_sum = image[seed_x, seed_y]
    region_count = 1
    stack = [(seed_x, seed_y)]
    visited[seed_x, seed_y] = True
    mask[seed_x, seed_y] = 255
    neighbor_offsets = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]
    while stack:
        x, y = stack.pop()
        region_mean = region_sum / region_count
        for dx, dy in neighbor_offsets:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx, ny]:
                visited[nx, ny] = True
                if abs(image[nx, ny] - region_mean) <= threshold:
                    mask[nx, ny] = 255
                    region_sum += image[nx, ny]
                    region_count += 1
                    stack.append((nx, ny))
    return mask
# ----

edge_configs = [
    {"path": "image1.jpg", "edge_threshold": 60},
    {"path": "image2.jpg", "edge_threshold": 60},
]

region_configs = [
    {"path": "image3.png", "seed": (50, 50), "region_threshold": 15},
    {"path": "image4.jpg", "seed": (50, 50), "region_threshold": 15},
]
# ----

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

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
for row, cfg in enumerate(region_configs):
    img = load_grayscale(cfg["path"])
    region_mask = region_growing(
        img,
        cfg["seed"],
        cfg["region_threshold"]
    )
    axes[row, 0].imshow(img, cmap='gray')
    axes[row, 0].set_title(f'{cfg["path"]} - Original')
    axes[row, 1].imshow(region_mask, cmap='gray')
    axes[row, 1].set_title('Region-Based Segmentation')
    for ax in axes[row]:
        ax.axis('off')
plt.tight_layout()
plt.show()
# ----
