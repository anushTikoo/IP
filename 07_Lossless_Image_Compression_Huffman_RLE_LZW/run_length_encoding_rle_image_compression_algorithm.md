# Algorithm Guide: Run-Length Encoding (RLE) Image Compression

## 1. Problem Statement & Objective
Compress digital images containing repetitive sequential pixel values by replacing contiguous runs with (run_length, pixel_value) tuples.

---

## 2. Input and Output Specifications
- **Input:** Binary or Grayscale image $I \in \mathbb{R}^{M \times N}$.
- **Output:** Encoded run-length list $[(L_1, V_1), (L_2, V_2), \dots]$, decoded image $I_{rec}$, and compression ratio $CR$.

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Flatten 2D image into 1D raster sequence $P$ of length $M \times N$.
- **Step 2:** Initialize `encoded_runs = []`, `current_val = P[0]`, `run_length = 1`.
- **Step 3:** Iterate through indices $k = 1, 2, \dots, M \cdot N - 1$:
- **Step 4:** If $P[k] == current\_val$, increment `run_length += 1`.
- **Step 5:** Else, append tuple `(run_length, current_val)` to `encoded_runs`; reset `current_val = P[k]` and `run_length = 1`.
- **Step 6:** Append the final active run `(run_length, current_val)` after loop completion.
- **Step 7 [Decoding]:** Reconstruct 1D stream by repeating each $V_i$ exactly $L_i$ times; reshape into original $M \times N$ matrix.
- **Step 8:** Compute Compression Ratio: $CR = \frac{M \times N}{\text{len(encoded\_runs)} \times 2}$.

---

## 4. Structured Pseudocode
```text
ALGORITHM RunLengthEncoding(Image I):
    P = flatten(I)
    N_pixels = length(P)
    runs = []

    curr_val = P[0]
    count = 1

    FOR k = 1 TO N_pixels - 1 DO:
        IF P[k] == curr_val THEN:
            count = count + 1
        ELSE:
            runs.append((count, curr_val))
            curr_val = P[k]
            count = 1
        END IF
    END FOR
    runs.append((count, curr_val))

    // Decoding
    decoded = []
    FOR EACH (count, val) IN runs DO:
        FOR c = 1 TO count DO:
            decoded.append(val)
        END FOR
    END FOR
    Reconstructed = reshape(decoded, I.shape)

    RETURN runs, Reconstructed
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **RLE Representation:** $R = \{ (l_k, v_k) \}_{k=1}^m \quad \text{such that } \sum_{k=1}^m l_k = M \times N$
- **Compression Ratio:** $CR = \frac{M \times N \times B_{pixel}}{m \times (B_{length} + B_{pixel})}$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N)$ linear single-pass scan across all pixels.
- **Space Complexity:** $O(M \times N)$ in the worst case (alternating noise), $O(m)$ in typical images.

---

## 7. Edge Cases & Boundary Handling
In alternating/noisy images (e.g. $0, 1, 0, 1, \dots$), RLE produces $M \times N$ tuples of length 1, expanding file size by $200\%$ ($CR = 0.5$).

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Conservation of pixel count: Sum of all run lengths strictly equals total image pixels: $\\sum L_i = M \\times N$.
- Deterministic invertibility: Exact mathematical identity between $I$ and $I_{rec}$.
