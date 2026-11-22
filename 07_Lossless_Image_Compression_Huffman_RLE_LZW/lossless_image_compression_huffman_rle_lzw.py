import heapq
import numpy as np
import matplotlib.pyplot as plt
from skimage import data
# ----

img = data.camera()
img = ((img // 16) * 16).astype(np.uint8)

# 1. Huffman Coding
class Node:
    def __init__(self, freq, sym=None, left=None, right=None):
        self.freq, self.sym, self.left, self.right = freq, sym, left, right
    def __lt__(self, other): return self.freq < other.freq

vals, cnts = np.unique(img, return_counts=True)
heap = [Node(c, v) for v, c in zip(vals, cnts)]
heapq.heapify(heap)
while len(heap) > 1:
    n1, n2 = heapq.heappop(heap), heapq.heappop(heap)
    heapq.heappush(heap, Node(n1.freq + n2.freq, left=n1, right=n2))

def get_codes(n, p=""):
    if n.sym is not None: return {n.sym: p}
    c = get_codes(n.left, p + "0"); c.update(get_codes(n.right, p + "1"))
    return c

huff_cb = get_codes(heap[0])
huff_bits = sum(len(huff_cb[p]) for p in img.ravel())
huff_cr = (img.size * 8) / huff_bits

# 2. RLE
data_flat = img.flatten()
rle_runs = 1 + sum(data_flat[i] != data_flat[i-1] for i in range(1, len(data_flat)))
rle_cr = img.nbytes / (rle_runs * 5)

# 3. LZW
d = {bytes([i]): i for i in range(256)}
curr, next_code, lzw_codes = b"", 256, 0
for p in data_flat:
    s = bytes([int(p)])
    if curr + s in d: curr += s
    else:
        lzw_codes += 1
        d[curr + s] = next_code
        next_code += 1
        curr = s
if curr: lzw_codes += 1
lzw_cr = img.nbytes / (lzw_codes * 2)
# ----

print(f\"Compression Ratios -> Huffman: {huff_cr:.2f}:1 | LZW: {lzw_cr:.2f}:1 | RLE: {rle_cr:.2f}:1\")

plt.figure(figsize=(6, 4))\nplt.bar([\"Huffman\", \"LZW\", \"RLE\"], [huff_cr, lzw_cr, rle_cr], color=['#2196F3', '#4CAF50', '#FF9800'])\nplt.ylabel(\"Compression Ratio (:1)\")\nplt.title(\"Lossless Compression Comparison\")\nplt.tight_layout()\nplt.show()\n# ----\n