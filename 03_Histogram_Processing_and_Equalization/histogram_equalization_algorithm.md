# Algorithm Guide: Global Histogram Equalization

## 1. Problem Statement & Objective
Automatically maximize image global contrast by transforming pixel intensities through their normalized Cumulative Distribution Function (CDF) to approximate a uniform intensity distribution.

---

## 2. Input and Output Specifications
- **Input:** Grayscale image $I \in \mathbb{R}^{M \times N}$ with $L = 256$ possible intensity levels.
- **Output:** Equalized image $I_{eq} \in \mathbb{R}^{M \times N}$ (`uint8`) and transformation look-up table $LUT \in \mathbb{R}^{256}$.

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Read input image or generate synthetic underexposed low-contrast image.
- **Step 2 [Histogram Computation]:** Initialize histogram array $H$ of length 256 with zeros. Iterate through all pixels in $I$ and increment $H[I(i, j)] \mathrel{+}= 1$.
- **Step 3 [CDF Computation]:** Compute running cumulative sum: $CDF[k] = \sum_{r=0}^k H[r]$ for $k = 0, 1, \dots, 255$. Total pixels $N_{total} = CDF[255] = M \times N$.
- **Step 4 [Look-Up Table (LUT) Construction]:** Map CDF values to the range $[0, 255]$: $LUT[k] = \text{round}\left( \frac{CDF[k]}{N_{total}} \times (L - 1) \right)$.
- **Step 5 [Vectorized Mapping]:** Apply LUT to replace every pixel in the image: $I_{eq} = LUT[I]$.
- **Step 6:** Display original and equalized images alongside their respective histograms and CDF curves.

---

## 4. Structured Pseudocode
```text
ALGORITHM HistogramEqualization(Image I):
    M, N = dimensions of I
    total_pixels = M * N
    Initialize Hist[256] with 0
    Initialize CDF[256] with 0
    Initialize LUT[256] as uint8

    // 1. Compute Histogram
    FOR EACH pixel IN flatten(I) DO:
        Hist[pixel] = Hist[pixel] + 1
    END FOR

    // 2. Compute CDF
    running_sum = 0
    FOR k = 0 TO 255 DO:
        running_sum = running_sum + Hist[k]
        CDF[k] = running_sum
    END FOR

    // 3. Construct Look-Up Table (LUT)
    FOR k = 0 TO 255 DO:
        LUT[k] = int(round((CDF[k] / total_pixels) * 255))
    END FOR

    // 4. Map Image
    Initialize Eq[M, N] as uint8
    FOR i = 0 TO M - 1 DO:
        FOR j = 0 TO N - 1 DO:
            Eq[i, j] = LUT[I[i, j]]
        END FOR
    END FOR

    RETURN Eq, LUT
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Probability Density Function (PDF):** $p_r(r_k) = \frac{n_k}{M \times N}, \quad k = 0, 1, \dots, L-1$
- **Cumulative Distribution Function (CDF):** $CDF(r_k) = \sum_{j=0}^k p_r(r_j)$
- **Equalization Transformation:** $s_k = T(r_k) = \text{round}\left( (L - 1) \sum_{j=0}^k \frac{n_j}{M \times N} \right)$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N + L)$ where $L=256$, achieving real-time performance.
- **Space Complexity:** $O(M \times N + L)$ memory for histogram, CDF, LUT, and output image.

---

## 7. Edge Cases & Boundary Handling
In discrete images, exact uniform distribution cannot be achieved because multiple pixels share identical intensities and must map to the same target bin (histogram flattening, not ideal uniformity).

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Monotonicity of CDF: $CDF[k] \ge CDF[k-1]$ for all $k$, ensuring that brightness order is preserved without intensity inversion.
- Maximum mapping: $CDF[255] = M \times N \implies LUT[255] = 255$.
