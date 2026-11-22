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
