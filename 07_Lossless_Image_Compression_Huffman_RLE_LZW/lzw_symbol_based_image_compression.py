import numpy as np
import matplotlib.pyplot as plt
import heapq
from collections import Counter
from skimage import data
from skimage.color import rgb2gray
from skimage.transform import resize
# ----

lzw_image = data.coffee()
lzw_image = rgb2gray(lzw_image)
lzw_image = resize(
    lzw_image,
    (256, 256),
    anti_aliasing=True
)
lzw_image = (
    lzw_image * 255
).astype(np.uint8)
levels = 16
lzw_image = (
    lzw_image // (256 // levels)
) * (256 // levels)
lzw_image = lzw_image.astype(
    np.uint8
)
# ----

def format_size(size):
    if size < 1024:
        return f"{size:.2f} Bytes"
    elif size < 1024 * 1024:
        return f"{size / 1024:.2f} KB"
    else:
        return f"{size / (1024 * 1024):.2f} MB"

def show_result(
    image_name,
    original,
    reconstructed,
    algorithm,
    original_size,
    compressed_size
):
    compression_ratio = (
        original_size /
        compressed_size
    )
    size_reduction = (
        1 -
        compressed_size /
        original_size
    ) * 100
    plt.figure(
        figsize=(12, 6)
    )
    plt.subplot(1, 2, 1)
    plt.imshow(
        original,
        cmap="gray"
    )
    plt.title(
        "Original Image"
    )
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(
        reconstructed,
        cmap="gray"
    )
    plt.title(
        "Compressed / Reconstructed"
    )
    plt.axis("off")
    plt.suptitle(
        f"{image_name} - {algorithm}",
        fontsize=16,
        fontweight="bold"
    )
    information = (
        f"Original Size: "
        f"{format_size(original_size)}\n"
        f"Compressed Size: "
        f"{format_size(compressed_size)}\n"
        f"Compression Ratio: "
        f"{compression_ratio:.2f}:1\n"
        f"Size Reduction: "
        f"{size_reduction:.2f}%"
    )
    plt.figtext(
        0.5,
        0.01,
        information,
        ha="center",
        fontsize=11
    )
    plt.tight_layout(
        rect=[
            0,
            0.13,
            1,
            0.93
        ]
    )
    plt.show()

    print("--------------------------------------------")
    print("Algorithm:", algorithm)
    print("Original Size:", format_size(original_size))
    print("Compressed Size:", format_size(compressed_size))
    print(
        "Compression Ratio:",
        f"{compression_ratio:.2f}:1"
    )
    print(
        "Size Reduction:",
        f"{size_reduction:.2f}%"
    )
    print("--------------------------------------------")
# ----

def lzw_compress(image):
    data = image.flatten()
    dictionary = {
        bytes([i]): i
        for i in range(256)
    }
    next_code = 256
    current = b""
    output = []
    for pixel in data:
        symbol = bytes([
            int(pixel)
        ])
        combined = (
            current + symbol
        )
        if combined in dictionary:
            current = combined
        else:
            output.append(
                dictionary[current]
            )
            dictionary[
                combined
            ] = next_code
            next_code += 1
            current = symbol
    if current:
        output.append(
            dictionary[current]
        )
    return output

def lzw_decompress(
    encoded,
    shape
):
    dictionary = {
        i: bytes([i])
        for i in range(256)
    }
    next_code = 256
    previous = bytes([
        encoded[0]
    ])
    output = bytearray(
        previous
    )
    for code in encoded[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = (
                previous +
                previous[:1]
            )
        else:
            raise ValueError(
                "Invalid LZW data"
            )
        output.extend(entry)
        dictionary[
            next_code
        ] = previous + entry[:1]
        next_code += 1
        previous = entry
    return np.frombuffer(
        output,
        dtype=np.uint8
    ).reshape(shape)
# ----

image = lzw_image
original_size = image.nbytes
encoded = lzw_compress(
    image
)
reconstructed = lzw_decompress(
    encoded,
    image.shape
)
compressed_size = (
    len(encoded) * 2
)
compression_ratio = (
    original_size /
    compressed_size
)
size_reduction = (
    1 -
    compressed_size /
    original_size
) * 100
show_result(
    "Coffee Image",
    image,
    reconstructed,
    "LZW SYMBOL-BASED ENCODING",
    original_size,
    compressed_size
)
print(
    "Number of gray levels:",
    len(np.unique(image))
)
print(
    "Number of LZW codes:",
    len(encoded)
)
print(
    "Original size:",
    format_size(original_size)
)
print(
    "Compressed size:",
    format_size(compressed_size)
)
print(
    "Compression ratio:",
    f"{compression_ratio:.2f}:1"
)
print(
    "Size reduction:",
    f"{size_reduction:.2f}%"
)
# ----
