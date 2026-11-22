# Algorithm Guide: Grayscale Conversion and Color Inversion

## 1. Problem Statement & Objective
Convert a multi-channel RGB image to a calibrated scalar luminance representation and compute channel-wise photographic color and grayscale negatives.

---

## 2. Input and Output Specifications
- **Input:** Color image $I_{RGB} \in \mathbb{R}^{M \times N \times 3}$, $R, G, B \in [0, 255]$.
- **Output:** Grayscale image $I_{gray} \in \mathbb{R}^{M \times N}$ and negative images $I_{neg\_rgb} \in \mathbb{R}^{M \times N \times 3}$, $I_{neg\_gray} \in \mathbb{R}^{M \times N}$.

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Check if input image exists on disk; if not, construct a synthetic RGB gradient test image.
- **Step 2:** Allocate 2D array $I_{gray}$ of dimensions $M \times N$ with type `uint8`.
- **Step 3:** Compute perceptual luminance for each spatial coordinate: $I_{gray}(i, j) = \text{round}(0.299 \cdot R(i, j) + 0.587 \cdot G(i, j) + 0.114 \cdot B(i, j))$.
- **Step 4:** Compute full RGB negative: $I_{neg\_rgb}(i, j, c) = 255 - I_{RGB}(i, j, c)$ for each channel $c \in \{0, 1, 2\}$.
- **Step 5:** Compute grayscale negative: $I_{neg\_gray}(i, j) = 255 - I_{gray}(i, j)$.
- **Step 6:** Display original RGB, Grayscale, Inverted RGB, and Inverted Grayscale using matplotlib.

---

## 4. Structured Pseudocode
```text
ALGORITHM GrayscaleAndInversion(Image RGB):
    M, N, C = dimensions of RGB
    Initialize Gray[M, N], NegRGB[M, N, C], NegGray[M, N] as uint8

    FOR i = 0 TO M - 1 DO:
        FOR j = 0 TO N - 1 DO:
            Gray[i, j] = int(0.299 * RGB[i, j, 0] + 0.587 * RGB[i, j, 1] + 0.114 * RGB[i, j, 2])
            NegGray[i, j] = 255 - Gray[i, j]
            
            FOR c = 0 TO 2 DO:
                NegRGB[i, j, c] = 255 - RGB[i, j, c]
            END FOR
        END FOR
    END FOR

    RETURN Gray, NegRGB, NegGray
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Perceptual Luminance:** $Y = 0.299R + 0.587G + 0.114B$
- **Negative Operator:** $T(r) = (L - 1) - r = 255 - r$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N)$ linear scan across all image pixels.
- **Space Complexity:** $O(M \times N)$ memory to hold output arrays.

---

## 7. Edge Cases & Boundary Handling
If the input is already a 2-dimensional single-channel array, skip luminance conversion and calculate negative directly.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Dynamic range preservation: Output intensities strictly reside within $[0, 255]$.
- Contrast symmetry: Maximum input intensity ($255$) maps to minimum ($0$) and vice versa.
