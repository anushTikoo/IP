# Algorithm Guide: Contrast Stretching (Min-Max Normalization)

## 1. Problem Statement & Objective
Expand the narrow dynamic range of low-contrast images across the full $[0, 255]$ intensity spectrum using linear and piecewise-linear intensity transformations.

---

## 2. Input and Output Specifications
- **Input:** Grayscale image $I \in \mathbb{R}^{M \times N}$, with pixel values in $[r_{min}, r_{max}]$, desired output range $[s_{min}, s_{max}] = [0, 255]$.
- **Output:** Contrast-stretched image $I_{stretch} \in \mathbb{R}^{M \times N}$ (`uint8`).

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Read input image or generate synthetic low-contrast image confined to a narrow intensity range $[50, 150]$.
- **Step 2:** Scan the image matrix to find the global minimum intensity $r_{min} = \min(I)$ and maximum intensity $r_{max} = \max(I)$.
- **Step 3:** Check degenerate condition: If $r_{max} == r_{min}$, the image is completely flat; return unchanged matrix to avoid division by zero.
- **Step 4:** For each pixel coordinate $(i, j)$, apply the linear stretch transformation: $I_{stretch}(i, j) = \text{round}\left( \frac{I(i, j) - r_{min}}{r_{max} - r_{min}} \times (s_{max} - s_{min}) + s_{min} \right)$.
- **Step 5:** Cast the stretched array to `uint8`.
- **Step 6:** Compute and plot histograms of original and contrast-stretched images to visually demonstrate dynamic range expansion.

---

## 4. Structured Pseudocode
```text
ALGORITHM ContrastStretching(Image I, int s_min=0, int s_max=255):
    M, N = dimensions of I
    r_min = min(I)
    r_max = max(I)

    IF r_max == r_min THEN:
        RETURN I  // Avoid division by zero
    END IF

    Initialize Stretched[M, N] as uint8
    scale = (s_max - s_min) / (r_max - r_min)

    FOR i = 0 TO M - 1 DO:
        FOR j = 0 TO N - 1 DO:
            val = (I[i, j] - r_min) * scale + s_min
            Stretched[i, j] = int(round(val))
        END FOR
    END FOR

    RETURN Stretched
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Linear Scaling Formula:** $s = T(r) = \frac{r - r_{min}}{r_{max} - r_{min}} \times (s_{max} - s_{min}) + s_{min}$
- **Standard 8-Bit Dynamic Range Mapping ($s_{min}=0, s_{max}=255$):** $s = \frac{r - r_{min}}{r_{max} - r_{min}} \times 255$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N)$ — one pass to compute min/max, and a second pass to stretch.
- **Space Complexity:** $O(M \times N)$ auxiliary storage for the output image.

---

## 7. Edge Cases & Boundary Handling
When $r_{max} == r_{min}$ (uniform image), division by zero occurs; algorithm intercepts this and returns original image.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Monotonicity: If $r_1 < r_2$, then $T(r_1) < T(r_2)$ (relative rank order of intensities is strictly preserved).
- Histogram shape: Relative frequency proportions of bins are preserved, but inter-bin gaps are linearly widened.
