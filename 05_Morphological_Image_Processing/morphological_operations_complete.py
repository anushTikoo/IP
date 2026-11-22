from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
# ----

def load_binary_image(filename, threshold=128):
    img = Image.open(filename).convert(\"L\")
    gray = np.array(img)
    binary = np.zeros(gray.shape, dtype=np.uint8)
    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):
            if gray[i, j] < threshold:
                binary[i, j] = 1
            else:
                binary[i, j] = 0
    return binary

filename = \"image.jpg\"
image = load_binary_image(filename)
print(\"Image loaded successfully!\")
print(\"Image shape:\", image.shape)\nprint(\"Pixel values:\", np.unique(image))
# ----

plt.figure(figsize=(6, 6))
plt.imshow(image, cmap=\"gray\")
plt.title(\"Original Binary Image\")
plt.axis(\"off\")
plt.show()
# ----

kernel = np.array([\n    [1, 1, 1],\n    [1, 1, 1],\n    [1, 1, 1]\n], dtype=np.uint8)
print(kernel)
# ----

def pad_image(image, pad):\n    h, w = image.shape
    padded = np.zeros(
        (h + 2 * pad, w + 2 * pad),
        dtype=np.uint8
    )
    for i in range(h):
        for j in range(w):
            padded[i + pad, j + pad] = image[i, j]
    return padded
# ----

def erosion(image, kernel):\n    kh, kw = kernel.shape
    pad_h = kh // 2
    pad_w = kw // 2
    padded = pad_image(image, max(pad_h, pad_w))
    h, w = image.shape
    output = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            fits = True
            for ki in range(kh):
                for kj in range(kw):
                    if kernel[ki, kj] == 1:
                        pi = i + ki
                        pj = j + kj
                        if padded[pi, pj] == 0:
                            fits = False
                            break
                if not fits:
                    break
            if fits:
                output[i, j] = 1
    return output
# ----

eroded = erosion(image, kernel)
plt.figure(figsize=(6, 6))
plt.imshow(eroded, cmap=\"gray\")
plt.title(\"Erosion\")
plt.axis(\"off\")
plt.show()
# ----

def dilation(image, kernel):\n    kh, kw = kernel.shape
    pad_h = kh // 2
    pad_w = kw // 2
    padded = pad_image(image, max(pad_h, pad_w))
    h, w = image.shape
    output = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            found = False
            for ki in range(kh):
                for kj in range(kw):
                    if kernel[ki, kj] == 1:
                        pi = i + ki
                        pj = j + kj
                        if padded[pi, pj] == 1:
                            found = True
                            break
                if found:
                    break
            if found:
                output[i, j] = 1
    return output
# ----

dilated = dilation(image, kernel)
plt.figure(figsize=(6, 6))
plt.imshow(dilated, cmap=\"gray\")
plt.title(\"Dilation\")
plt.axis(\"off\")
plt.show()
# ----

def opening(image, kernel):\n    eroded = erosion(image, kernel)
    result = dilation(eroded, kernel)
    return result

opened = opening(image, kernel)
plt.figure(figsize=(6, 6))
plt.imshow(opened, cmap=\"gray\")
plt.title(\"Opening\")
plt.axis(\"off\")
plt.show()
# ----

def closing(image, kernel):\n    dilated = dilation(image, kernel)
    result = erosion(dilated, kernel)
    return result

closed = closing(image, kernel)
plt.figure(figsize=(6, 6))
plt.imshow(closed, cmap=\"gray\")
plt.title(\"Closing\")
plt.axis(\"off\")
plt.show()
# ----

def connected_components(image):\n    h, w = image.shape
    visited = np.zeros((h, w), dtype=np.uint8)
    components = []
    neighbors = [\n        (-1, -1), (-1, 0), (-1, 1),\n        (0, -1),           (0, 1),\n        (1, -1),  (1, 0),  (1, 1)\n    ]
    for i in range(h):
        for j in range(w):
            if image[i, j] == 1 and visited[i, j] == 0:
                queue = [(i, j)]
                visited[i, j] = 1
                component = []
                front = 0
                while front < len(queue):
                    x, y = queue[front]
                    front += 1
                    component.append((x, y))
                    for dx, dy in neighbors:
                        nx = x + dx
                        ny = y + dy
                        if (
                            0 <= nx < h and
                            0 <= ny < w and
                            image[nx, ny] == 1 and
                            visited[nx, ny] == 0
                        ):
                            visited[nx, ny] = 1
                            queue.append((nx, ny))
                components.append(component)
    return components
# ----

components = connected_components(image)
print(\"Number of connected components:\", len(components))
for i, component in enumerate(components):
    print(f\"Component {i + 1}: {len(component)} pixels\")
# ----

def remove_small_objects(image, minimum_size):\n    components = connected_components(image)
    output = np.zeros_like(image)
    for component in components:
        if len(component) >= minimum_size:
            for x, y in component:
                output[x, y] = 1
    return output

minimum_size = 50
small_objects_removed = remove_small_objects(
    image,
    minimum_size
)
plt.figure(figsize=(6, 6))
plt.imshow(small_objects_removed, cmap=\"gray\")
plt.title(f\"Small Objects Removed (Minimum Size = {minimum_size})\")
plt.axis(\"off\")
plt.show()
# ----

def extract_boundary(image, kernel):\n    eroded = erosion(image, kernel)
    h, w = image.shape
    boundary = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if image[i, j] == 1 and eroded[i, j] == 0:
                boundary[i, j] = 1
    return boundary

boundary = extract_boundary(image, kernel)
plt.figure(figsize=(6, 6))
plt.imshow(boundary, cmap=\"gray\")
plt.title(\"Boundary Extraction\")
plt.axis(\"off\")
plt.show()
# ----

def count_neighbors(image, i, j):\n    neighbors = [\n        image[i-1, j],\n        image[i-1, j+1],\n        image[i, j+1],\n        image[i+1, j+1],\n        image[i+1, j],\n        image[i+1, j-1],\n        image[i, j-1],\n        image[i-1, j-1]\n    ]
    return sum(neighbors)

def transitions(image, i, j):\n    pixels = [\n        image[i-1, j],\n        image[i-1, j+1],\n        image[i, j+1],\n        image[i+1, j+1],\n        image[i+1, j],\n        image[i+1, j-1],\n        image[i, j-1],\n        image[i-1, j-1]\n    ]
    pixels.append(pixels[0])
    count = 0
    for k in range(8):
        if pixels[k] == 0 and pixels[k+1] == 1:
            count += 1
    return count
# ----

def skeletonize(image):\n    img = image.copy()
    changed = True
    while changed:
        changed = False
        h, w = img.shape
        to_delete = []
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                if img[i, j] != 1:
                    continue
                B = count_neighbors(img, i, j)
                A = transitions(img, i, j)
                p2 = img[i-1, j]
                p4 = img[i, j+1]
                p6 = img[i+1, j]
                p8 = img[i, j-1]
                if (
                    2 <= B <= 6 and
                    A == 1 and
                    p2 * p4 * p6 == 0 and
                    p4 * p6 * p8 == 0
                ):
                    to_delete.append((i, j))
        for i, j in to_delete:
            img[i, j] = 0
        if len(to_delete) > 0:
            changed = True

        to_delete = []
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                if img[i, j] != 1:
                    continue
                B = count_neighbors(img, i, j)
                A = transitions(img, i, j)
                p2 = img[i-1, j]
                p4 = img[i, j+1]
                p6 = img[i+1, j]
                p8 = img[i, j-1]
                if (
                    2 <= B <= 6 and
                    A == 1 and
                    p2 * p4 * p8 == 0 and
                    p2 * p6 * p8 == 0
                ):
                    to_delete.append((i, j))
        for i, j in to_delete:
            img[i, j] = 0
        if len(to_delete) > 0:
            changed = True
    return img
# ----

skeleton = skeletonize(image)
plt.figure(figsize=(6, 6))
plt.imshow(skeleton, cmap=\"gray\")
plt.title(\"Skeletonization\")
plt.axis(\"off\")
plt.show()
# ----

plt.figure(figsize=(14, 8))
results = [\n    (image, \"Original\"),\n    (eroded, \"Erosion\"),\n    (dilated, \"Dilation\"),\n    (opened, \"Opening\"),\n    (closed, \"Closing\"),\n    (small_objects_removed, \"Small Objects Removed\"),\n    (boundary, \"Boundary\"),\n    (skeleton, \"Skeleton\")\n]
for index, (result, title) in enumerate(results):
    plt.subplot(2, 4, index + 1)
    plt.imshow(result, cmap=\"gray\")
    plt.title(title)
    plt.axis(\"off\")
plt.tight_layout()
plt.show()
# ----
