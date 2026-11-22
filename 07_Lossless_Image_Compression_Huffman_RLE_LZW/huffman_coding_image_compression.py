import heapq
import numpy as np
import matplotlib.pyplot as plt
from skimage import data
# ----

img = data.camera()
# Quantize to 16 levels for compact compression demonstration
img = ((img // 16) * 16).astype(np.uint8)
# ----

class Node:
    def __init__(self, freq, symbol=None, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(pixels):
    values, counts = np.unique(pixels, return_counts=True)
    heap = [Node(freq=c, symbol=v) for v, c in zip(values, counts)]
    heapq.heapify(heap)
    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        heapq.heappush(heap, Node(freq=n1.freq + n2.freq, left=n1, right=n2))
    return heap[0]

def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}
    if node.symbol is not None:
        codebook[node.symbol] = prefix
    else:
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook
# ----

tree = build_huffman_tree(img)
codebook = generate_codes(tree)
encoded_bits = "".join(codebook[p] for p in img.ravel())

orig_bits = img.size * 8
comp_bits = len(encoded_bits)
print(f"Original: {orig_bits} bits | Compressed: {comp_bits} bits | Ratio: {orig_bits / comp_bits:.2f}:1")

# Decode back
decoded = []
current = tree
for bit in encoded_bits:
    current = current.left if bit == "0" else current.right
    if current.symbol is not None:
        decoded.append(current.symbol)
        current = tree
recon = np.array(decoded, dtype=np.uint8).reshape(img.shape)
# ----

plt.figure(figsize=(8, 4))\nplt.subplot(121); plt.imshow(img, cmap=\"gray\"); plt.title(\"Original (16 levels)\"); plt.axis(\"off\")\nplt.subplot(122); plt.imshow(recon, cmap=\"gray\"); plt.title(f\"Huffman Decoded (CR: {orig_bits/comp_bits:.2f}:1)\"); plt.axis(\"off\")\nplt.tight_layout()\nplt.show()\n# ----\n