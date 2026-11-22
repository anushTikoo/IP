# Viva & Theory Guide: Lempel-Ziv-Welch (LZW) Image Compression

## 1. First-Principles Analogy
> Imagine writing notes in a fast-paced lecture. The first time the professor says "Convolutional Neural Network", you write the whole phrase down and write "CNN = 1". The next time the professor says it, you just write "1". As more multi-word phrases repeat, you assign them numbers. Both you and anyone reading your notebook can build the exact same numbered dictionary on the fly without needing a separate dictionary passed between you.

---

## 2. What It Is (Concept & Definition)
- **LZW Compression**: A universal, dictionary-based, lossless compression algorithm developed by Terry Welch in 1984 (building on Lempel-Ziv LZ78).
- **Core Concept**: Replaces repeated variable-length sequences of bytes (phrases) with fixed-length numeric index codes pointing to a dynamically generated dictionary table.
- **The Revolutionary Breakthrough**: The dictionary is **never transmitted with the compressed data**! The decompressor reconstructs the identical dictionary dynamically on the fly during single-pass decoding.
- **Standard Formats**: The fundamental compression engine of **GIF** (Graphics Interchange Format) and **TIFF**.

---

## 3. Why We Do It (Motivation & Practical Use Cases)
- **Adaptive to Local Structure**: Exploits multi-pixel patterns and repeating motifs without requiring prior statistical knowledge of symbol frequencies.
- **Single-Pass Stream Processing**: Compresses data in a single forward pass without needing to buffer the whole image first.
- **Lossless Fidelity**: Exact pixel preservation, ideal for computer-generated art, screenshots, graphics, and palette images.

---

## 4. How It Works (Algorithmic & Mathematical Breakdown)

### A. Compression Algorithm
1. **Initialize Dictionary**: Pre-fill dictionary with all 256 single-byte roots:

   $$
   \text{Dict}[0] = [0], \text{Dict}[1] = [1], \dots, \text{Dict}[255] = [255]
   $$
   Next available code index = $256$.
2. Set prefix string $P = \text{empty}$.
3. For each incoming pixel byte $C$:
   - Check if phrase $P + C$ exists in the dictionary.
   - If **YES**: $P = P + C$ (keep extending the phrase).
   - If **NO**:
     - Output the dictionary index code for $P$.
     - Add new phrase $P + C$ to the dictionary at the next available code index.
     - Reset $P = C$.
4. Output the code for remaining prefix $P$.

### B. Decompression Algorithm (The Symmetry)
1. Initialize dictionary with all 256 single-byte roots.
2. Read first code $OLD$; output its translation string.
3. For each subsequent code $NEW$:
   - Check if $NEW$ is in dictionary:
     - If **YES**: string $S = \text{Dict}[NEW]$.
     - If **NO** (The $cScSc$ Special Case): $S = \text{Dict}[OLD] + \text{Dict}[OLD][0]$.
   - Output string $S$.
   - Add $\text{Dict}[OLD] + S[0]$ to the dictionary.
   - Set $OLD = NEW$.

---

## 5. Code Walkthrough & Working

In [`lzw_symbol_based_image_compression.py`](file:///home/anushtikoo/Downloads/IP/07_Lossless_Image_Compression_Huffman_RLE_LZW/lzw_symbol_based_image_compression.py):
- **Cell 1**: Imports `numpy` and `matplotlib.pyplot`.
- **Cell 2**: Synthetic image quantized to 16 gray levels to highlight multi-pixel phrase repetition.
- **Cell 3**: First-principles LZW Encoder and Decoder:
  - `lzw_compress(image)`: Uses Python dictionary mapping byte-tuples to integer tokens. Outputs integer list `encoded`.
  - `lzw_decompress(encoded, shape)`: Reconstructs byte stream using dynamic dictionary expansion and handles the boundary condition where `code == dict_size`.
  - Computes Compression Ratio: `img.nbytes / (len(encoded) * 2)` (assuming 16-bit dictionary tokens).
- **Cell 4**: Lossless verification: tests `np.array_equal(img, recon)` and displays original vs decoded.

---

## 6. High-Yield Viva Questions & Examiner Traps

### Q1: Why does LZW not need to save or transmit the dictionary across the network?
**Answer**: Because the dictionary is constructed deterministically from the incoming sequence of data. The decompression algorithm follows the exact same logical rules as the compression algorithm. For every code it decodes, it knows what string was just emitted and takes the first character of the new string to assemble the exact same new dictionary entry at the exact same index.

### Q2: What is the famous "KwKwK" (or $cScSc$) edge case in LZW decompression?
**Answer**: This occurs when the encoder encounters a pattern consisting of a string $K$, followed by character $w$, repeated immediately ($KwKwK$). The encoder adds $KwK$ to the dictionary and immediately outputs that newly created code in the very next step. When the decoder receives this code, the code does not yet exist in its dictionary! The decoder handles this edge case by recognizing that $NEW = \text{dict\_size}$, meaning the missing string is simply $OLD + OLD[0]$.

### Q3: How is dictionary overflow handled when the dictionary reaches its maximum size (e.g., 4096 entries for 12-bit codes)?
**Answer**: Real-world implementations (like GIF) use two approaches:
1. **Freeze Dictionary**: Stop adding new phrases and use the existing dictionary as a static codebook for the remainder of the file.
2. **Clear Table (Reset)**: Emit a special reserved "Clear Code", discard the entire dictionary, reset back to the initial 256 roots, and start building new phrases adapted to the new image regions.
