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
