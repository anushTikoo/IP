import numpy as np
import matplotlib.pyplot as plt
import heapq
from collections import Counter
from skimage import data
from skimage.color import rgb2gray
from skimage.transform import resize
# ----

rle_image = np.zeros(
    (256, 256),
    dtype=np.uint8
)
rle_image[0:60, :] = 0
rle_image[60:120, :] = 50
rle_image[120:180, :] = 150
rle_image[180:220, :] = 200
rle_image[220:256, :] = 255
rle_image[70:110, 40:210] = 100
rle_image[130:170, 60:190] = 180
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

def rle_compress(image):
    data = image.flatten()
    values = []
    counts = []
    current_value = data[0]
    count = 1
    for pixel in data[1:]:
        if pixel == current_value:
            count += 1
        else:
            values.append(
                current_value
            )
            counts.append(
                count
            )
            current_value = pixel
            count = 1
    values.append(
        current_value
    )
    counts.append(
        count
    )
    return (
        np.array(
            values,
            dtype=np.uint8
        ),
        np.array(
            counts,
            dtype=np.uint32
        )
    )

def rle_decompress(
    values,
    counts,
    shape
):
    decoded = np.repeat(
        values,
        counts
    )
    return decoded.astype(
        np.uint8
    ).reshape(shape)
# ----

image = rle_image
original_size = image.nbytes
values, counts = rle_compress(
    image
)
reconstructed = rle_decompress(
    values,
    counts,
    image.shape
)
number_of_runs = len(values)
compressed_size = (
    number_of_runs * 5
)
show_result(
    "Long-Run Image",
    image,
    reconstructed,
    "RUN LENGTH ENCODING (RLE)",
    original_size,
    compressed_size
)
print(
    "Number of RLE runs:",
    number_of_runs
)
# ----
