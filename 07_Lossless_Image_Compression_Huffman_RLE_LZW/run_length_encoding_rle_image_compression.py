import numpy as np
import matplotlib.pyplot as plt
# ----

# Synthetic image with long runs
img = np.zeros((128, 128), dtype=np.uint8)
img[30:70, :] = 100
img[70:110, :] = 200
# ----

def rle_compress(image):
    data = image.flatten()
    values, counts = [], []
    curr, count = data[0], 1
    for p in data[1:]:
        if p == curr:
            count += 1
        else:
            values.append(curr)
            counts.append(count)
            curr, count = p, 1
    values.append(curr)
    counts.append(count)
    return np.array(values, dtype=np.uint8), np.array(counts, dtype=np.uint32)

def rle_decompress(values, counts, shape):
    return np.repeat(values, counts).reshape(shape)
# ----

values, counts = rle_compress(img)
recon = rle_decompress(values, counts, img.shape)

orig_size = img.nbytes
comp_size = len(values) * 5  # 1 byte for value + 4 bytes for count
print(f"Original: {orig_size} B | Compressed: {comp_size} B | Ratio: {orig_size / comp_size:.2f}:1")

plt.figure(figsize=(8, 4))\nplt.subplot(121); plt.imshow(img, cmap=\"gray\"); plt.title(\"Original\"); plt.axis(\"off\")\nplt.subplot(122); plt.imshow(recon, cmap=\"gray\"); plt.title(f\"RLE Decoded (CR: {orig_size/comp_size:.2f}:1)\"); plt.axis(\"off\")\nplt.tight_layout()\nplt.show()\n# ----\n