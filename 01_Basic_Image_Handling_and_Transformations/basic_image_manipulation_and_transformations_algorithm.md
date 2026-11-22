# Algorithm Guide: Basic Image Manipulation and Point Transformations

## 1. Problem Statement & Objective
Perform fundamental spatial and point operations including grayscale conversion, negative transformation, brightness/contrast scaling, and spatial reflections (flipping) from first principles.

---

## 2. Input and Output Specifications
- **Input:** Color (RGB) or Grayscale image matrix $I$ of size $M \times N \times 3$ or $M \times N$, with intensity values in $[0, 255]$ (`uint8`). Transformation parameters: brightness offset $\beta \in [-255, 255]$, contrast scale $\alpha > 0$.
- **Output:** Transformed image matrices: Grayscale $I_{gray}$, Negative $I_{neg}$, Adjusted $I_{adj}$, and Flipped matrices $I_{hflip}, I_{vflip}$ (`uint8`).

---

## 3. Step-by-Step Formal Algorithm
- **Step 1 [Input Acquisition]:** Read the input image from file path; if unavailable, generate a synthetic RGB test image with distinct geometric structures.
- **Step 2 [Grayscale Conversion]:** For each pixel $(i, j)$, extract color components $R(i, j), G(i, j), B(i, j)$ and compute the scalar luminance $Y(i, j) = 0.299 \cdot R(i, j) + 0.587 \cdot G(i, j) + 0.114 \cdot B(i, j)$. Cast result to unsigned 8-bit integer.
- **Step 3 [Negative Transformation]:** For each pixel $(i, j)$ in $I_{gray}$, compute inverted intensity $I_{neg}(i, j) = 255 - I_{gray}(i, j)$.
- **Step 4 [Brightness & Contrast Adjustment]:** For each pixel $(i, j)$, evaluate $I_{adj}(i, j) = \text{clip}(\alpha \cdot I_{gray}(i, j) + \beta, 0, 255)$ where $\text{clip}(v, 0, 255) = \min(\max(v, 0), 255)$.
- **Step 5 [Horizontal Flipping]:** Create matrix $I_{hflip}$ of size $M \times N$ by reversing column indices: $I_{hflip}(i, j) = I(i, N - 1 - j)$ for all $0 \le i < M$ and $0 \le j < N$.
- **Step 6 [Vertical Flipping]:** Create matrix $I_{vflip}$ of size $M \times N$ by reversing row indices: $I_{vflip}(i, j) = I(M - 1 - i, j)$ for all $0 \le i < M$ and $0 \le j < N$.
- **Step 7 [Visualization]:** Render input and all five transformed representations side-by-side using a multi-panel subplot layout.

---

## 4. Structured Pseudocode
```text
ALGORITHM BasicImageManipulation(Image I, float alpha, int beta):
    M, N, C = dimensions of I
    Initialize I_gray[M, N], I_neg[M, N], I_adj[M, N] as uint8
    Initialize I_hflip[M, N, C], I_vflip[M, N, C] as uint8

    // 1. Grayscale Conversion & Point Transformations
    FOR i = 0 TO M - 1 DO:
        FOR j = 0 TO N - 1 DO:
            I_gray[i, j] = int(0.299 * I[i, j, 0] + 0.587 * I[i, j, 1] + 0.114 * I[i, j, 2])
            I_neg[i, j]  = 255 - I_gray[i, j]
            
            val = alpha * I_gray[i, j] + beta
            I_adj[i, j] = max(0, min(255, int(val)))
        END FOR
    END FOR

    // 2. Spatial Flipping
    FOR i = 0 TO M - 1 DO:
        FOR j = 0 TO N - 1 DO:
            I_hflip[i, j] = I[i, N - 1 - j]
            I_vflip[i, j] = I[M - 1 - i, j]
        END FOR
    END FOR

    RETURN I_gray, I_neg, I_adj, I_hflip, I_vflip
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Luminance (ITU-R BT.601):** $Y(i, j) = 0.299 R(i, j) + 0.587 G(i, j) + 0.114 B(i, j)$
- **Image Inversion (Negative):** $s = (L - 1) - r = 255 - r$
- **Linear Point Transformation:** $s = \text{clip}(\alpha \cdot r + \beta, 0, 255)$
- **Coordinate Inversion:** Horizontal: $(x', y') = (N - 1 - x, y)$; Vertical: $(x', y') = (x, M - 1 - y)$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N)$ — each pixel is visited a constant number of times.
- **Space Complexity:** $O(M \times N)$ auxiliary storage for output representations.

---

## 7. Edge Cases & Boundary Handling
Integer arithmetic overflow ($> 255$) or underflow ($< 0$) must be saturated/clipped before assigning to `uint8`.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Luminance weights sum identically to $1.0$ ($0.299 + 0.587 + 0.114 = 1.0$), ensuring the maximum output cannot exceed 255.
- Involution property: $I_{neg}(I_{neg}(I)) = I$ and $I_{flip}(I_{flip}(I)) = I$.
