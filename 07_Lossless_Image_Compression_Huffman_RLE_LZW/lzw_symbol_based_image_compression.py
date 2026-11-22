import numpy as np
import matplotlib.pyplot as plt
from skimage import data
# ----

img = data.camera()
img = ((img // 16) * 16).astype(np.uint8)
# ----

def lzw_compress(image):
    data = image.flatten()
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    current = b""
    encoded = []
    for pixel in data:
        symbol = bytes([int(pixel)])
        combined = current + symbol
        if combined in dictionary:
            current = combined
        else:
            encoded.append(dictionary[current])
            dictionary[combined] = next_code
            next_code += 1
            current = symbol
    if current:
        encoded.append(dictionary[current])
    return encoded

def lzw_decompress(encoded, shape):
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    previous = bytes([encoded[0]])
    decoded = bytearray(previous)
    for code in encoded[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = previous + previous[:1]
        decoded.extend(entry)
        dictionary[next_code] = previous + entry[:1]
        next_code += 1
        previous = entry
    return np.frombuffer(decoded, dtype=np.uint8).reshape(shape)
# ----

encoded = lzw_compress(img)
recon = lzw_decompress(encoded, img.shape)

orig_bytes = img.nbytes
comp_bytes = len(encoded) * 2  # 16-bit codes
print(f"Original: {orig_bytes} B | Compressed: {comp_bytes} B | Ratio: {orig_bytes / comp_bytes:.2f}:1")

plt.figure(figsize=(8, 4))\nplt.subplot(121); plt.imshow(img, cmap=\"gray\"); plt.title(\"Original\"); plt.axis(\"off\")\nplt.subplot(122); plt.imshow(recon, cmap=\"gray\"); plt.title(f\"LZW Decoded (CR: {orig_bytes/comp_bytes:.2f}:1)\"); plt.axis(\"off\")\nplt.tight_layout()\nplt.show()\n# ----\n