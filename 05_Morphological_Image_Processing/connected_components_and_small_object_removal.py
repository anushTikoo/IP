from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
# ----

def load_binary_image(filename, threshold=128):
    img = Image.open(filename).convert("L")
    gray = np.array(img)
    binary = np.zeros(gray.shape, dtype=np.uint8)
    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):
            if gray[i, j] < threshold:
                binary[i, j] = 1
            else:
                binary[i, j] = 0
    return binary

filename = "image.jpg"
image = load_binary_image(filename)
print("Image loaded successfully!")
print("Image shape:", image.shape)
print("Pixel values:", np.unique(image))
# ----

def connected_components(image):
    h, w = image.shape
    visited = np.zeros((h, w), dtype=np.uint8)
    components = []
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
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
print("Number of connected components:", len(components))
for i, component in enumerate(components):
    print(f"Component {i + 1}: {len(component)} pixels")
# ----

def remove_small_objects(image, minimum_size):
    components = connected_components(image)
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
plt.imshow(small_objects_removed, cmap="gray")
plt.title(f"Small Objects Removed (Minimum Size = {minimum_size})")
plt.axis("off")
plt.show()
# ----
