# Algorithm Guide: Huffman Coding Lossless Image Compression

## 1. Problem Statement & Objective
Compress image pixel data losslessly by constructing an optimal prefix binary tree based on empirical symbol probability distributions.

---

## 2. Input and Output Specifications
- **Input:** Grayscale image $I \in \mathbb{R}^{M \times N}$ (`uint8`).
- **Output:** Encoded bitstring, prefix code dictionary `dict[symbol -> bitstring]`, reconstructed image $I_{rec}$, compression ratio $CR$, and Shannon entropy $H$.

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Flatten 2D image into 1D array of $M \times N$ symbols.
- **Step 2 [Frequency Analysis]:** Count frequency of each unique intensity value $s \in [0, 255]$ and compute empirical probabilities $p_i = \text{freq}_i / (M \cdot N)$.
- **Step 3 [Priority Queue / Min-Heap Initialization]:** Create a leaf node for each symbol with non-zero frequency and insert into min-heap ordered by frequency.
- **Step 4 [Tree Construction]:** While min-heap contains more than 1 node: pop the two lowest frequency nodes $n_1$ and $n_2$; create a new internal node with combined frequency $f = n_1.freq + n_2.freq$, left child $n_1$, and right child $n_2$; push new node into min-heap. The last remaining node is the root.
- **Step 5 [Prefix Code Generation]:** Recursively traverse tree from root down: append '0' for left edge, '1' for right edge. Assign leaf paths as canonical prefix codes.
- **Step 6 [Encoding]:** Map each pixel in 1D array to its binary codeword; concatenate into single bitstream.
- **Step 7 [Decoding]:** Traverse tree from root using successive bits from bitstream: when reaching a leaf, output its symbol and reset to root. Repeat until all $M \times N$ pixels are recovered.
- **Step 8:** Compute Compression Ratio $CR = \frac{8 \cdot M \cdot N}{\text{total compressed bits}}$ and verify $I_{rec} == I$ identically.

---

## 4. Structured Pseudocode
```text
ALGORITHM HuffmanCoding(Image I):
    symbols = flatten(I)
    frequencies = CountFrequencies(symbols)
    
    // Priority queue of (frequency, Node)
    heap = InitializeMinHeap(frequencies)

    WHILE heap.size() > 1 DO:
        n1 = heap.pop_min()
        n2 = heap.pop_min()
        parent = Node(freq = n1.freq + n2.freq, left = n1, right = n2)
        heap.insert(parent)
    END WHILE

    root = heap.pop_min()
    codebook = GenerateCodes(root, current_code="")

    // Encoding
    bitstring = ""
    FOR EACH s IN symbols DO:
        bitstring += codebook[s]
    END FOR

    // Decoding
    decoded = []
    curr = root
    FOR EACH bit IN bitstring DO:
        IF bit == '0' THEN curr = curr.left
        ELSE curr = curr.right
        
        IF curr.is_leaf() THEN:
            decoded.append(curr.symbol)
            curr = root
        END IF
    END FOR

    Reconstructed = reshape(decoded, I.shape)
    RETURN bitstring, codebook, Reconstructed
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Shannon Entropy (Theoretical Lower Bound):** $H(X) = -\sum_{i=1}^K p(s_i) \log_2 p(s_i) \quad \text{bits/pixel}$
- **Average Code Length:** $L_{avg} = \sum_{i=1}^K p(s_i) l(s_i) \quad \text{where } H(X) \le L_{avg} < H(X) + 1$
- **Compression Ratio:** $CR = \frac{B_{uncompressed}}{B_{compressed}} = \frac{8}{L_{avg}}$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N + K \log K)$ where $K \le 256$ is the alphabet size (executes near-instantaneously).
- **Space Complexity:** $O(M \times N)$ auxiliary storage for the encoded bitstream and reconstructed array.

---

## 7. Edge Cases & Boundary Handling
If image is completely uniform (all pixels identical, $K=1$), Huffman tree has 1 node; assign fixed single-bit code '0' to avoid infinite recursion.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Prefix property: No valid codeword is a prefix of any other codeword, ensuring instantaneous deterministic decoding without lookahead delimiters.
- Losslessness: Mean Squared Error $MSE(I, I_{rec}) = 0.0$ identically.
