import numpy as np
import matplotlib.pyplot as plt
import heapq
from collections import Counter
from skimage import data
from skimage.color import rgb2gray
from skimage.transform import resize
# ----

huffman_image = data.camera()
huffman_image = resize(
    huffman_image,
    (256, 256),
    anti_aliasing=True
)
huffman_image = (
    huffman_image * 255
).astype(np.uint8)

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

images = {
    "Camera": huffman_image,
    "RLE Long Runs": rle_image,
    "Coffee": lzw_image
}

plt.figure(
    figsize=(15, 5)
)
plt.subplot(1, 3, 1)
plt.imshow(
    huffman_image,
    cmap="gray"
)
plt.title(
    "Huffman - Camera"
)
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(
    rle_image,
    cmap="gray"
)
plt.title(
    "RLE - Long Runs"
)
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(
    lzw_image,
    cmap="gray"
)
plt.title(
    "LZW - Coffee (16 Gray Levels)"
)
plt.axis("off")

plt.tight_layout()
plt.show()

print(
    "LZW image gray levels:",
    len(np.unique(lzw_image))
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
        f"{format_size(original_size)}\\n"
        f"Compressed Size: "
        f"{format_size(compressed_size)}\\n"
        f"Compression Ratio: "
        f"{compression_ratio:.2f}:1\\n"
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

class HuffmanNode:
    def __init__(
        self,
        frequency,
        symbol=None,
        left=None,
        right=None
    ):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(image):
    frequency = Counter(
        image.flatten()
    )
    heap = []
    for symbol, freq in frequency.items():
        heap.append(
            HuffmanNode(
                freq,
                symbol
            )
        )
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = HuffmanNode(
            left.frequency + right.frequency,
            left=left,
            right=right
        )
        heapq.heappush(
            heap,
            parent
        )
    return heap[0]

def generate_codes(
    node,
    code="",
    codes=None
):
    if codes is None:
        codes = {}
    if node.symbol is not None:
        codes[node.symbol] = (
            code if code else "0"
        )
        return codes
    generate_codes(
        node.left,
        code + "0",
        codes
    )
    generate_codes(
        node.right,
        code + "1",
        codes
    )
    return codes

def huffman_compress(image):
    root = build_huffman_tree(image)
    codes = generate_codes(root)
    encoded = "".join(
        codes[pixel]
        for pixel in image.flatten()
    )
    return encoded, codes

def huffman_decompress(
    encoded,
    codes,
    shape
):
    reverse_codes = {
        value: key
        for key, value in codes.items()
    }
    current = ""
    decoded = []
    for bit in encoded:
        current += bit
        if current in reverse_codes:
            decoded.append(
                reverse_codes[current]
            )
            current = ""
    return np.array(
        decoded,
        dtype=np.uint8
    ).reshape(shape)
# ----

image = huffman_image
original_size = image.nbytes

encoded, codes = huffman_compress(
    image
)
reconstructed = huffman_decompress(
    encoded,
    codes,
    image.shape
)
encoded_bytes = (
    len(encoded) + 7
) // 8
dictionary_bytes = (
    len(codes) * 2
)
compressed_size = (
    encoded_bytes +
    dictionary_bytes
)
show_result(
    "Camera Image",
    image,
    reconstructed,
    "HUFFMAN CODING",
    original_size,
    compressed_size
)
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
