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

kernel = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
], dtype=np.uint8)
print(kernel)
# ----

def pad_image(image, pad):
    h, w = image.shape
    padded = np.zeros(
        (h + 2 * pad, w + 2 * pad),
        dtype=np.uint8
    )
    for i in range(h):
        for j in range(w):
            padded[i + pad, j + pad] = image[i, j]
    return padded
# ----

def erosion(image, kernel):
    kh, kw = kernel.shape
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
plt.imshow(eroded, cmap="gray")
plt.title("Erosion")
plt.axis("off")
plt.show()
# ----

def dilation(image, kernel):
    kh, kw = kernel.shape
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
plt.imshow(dilated, cmap="gray")
plt.title("Dilation")
plt.axis("off")
plt.show()
# ----
