# Algorithm Guide: Filtering with Non-Linear Min Filter

## 1. Problem Statement & Objective
Apply morphological erosion-like intensity filtering by replacing center pixels with local minimum neighborhood values, extinguishing salt noise.

---

## 2. Input and Output Specifications
- **Input:** Grayscale image $I \in \mathbb{R}^{M \times N}$, window size $K = 3$.
- **Output:** Min-filtered image $I_{min} \in \mathbb{R}^{M \times N}$ (`uint8`).

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Read input grayscale image or synthesize test image with bright noise spikes (salt).
- **Step 2:** Allocate output image $I_{min}$ of shape $M \times N$ with data type `uint8`.
- **Step 3:** Loop through interior coordinates $(i, j)$ where $1 \le i < M - 1$ and $1 \le j < N - 1$.
- **Step 4:** Slice $3 \times 3$ window: $R = I[i-1:i+2, j-1:j+2]$.
- **Step 5:** Compute minimum value: $I_{min}(i, j) = \min(R)$.
- **Step 6:** Display original and min-filtered images.

---

## 4. Structured Pseudocode
```text
ALGORITHM MinFilter(Image I, int window_size):
    M, N = dimensions of I
    r = window_size // 2
    Initialize Out[M, N] as uint8

    FOR i = r TO M - 1 - r DO:
        FOR j = r TO N - 1 - r DO:
            window = I[i - r : i + r + 1, j - r : j + r + 1]
            Out[i, j] = min(window)
        END FOR
    END FOR

    RETURN Out
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Min Filter Equation:** $g(x, y) = \min_{(s, t) \in W} \{ f(x+s, y+t) \}$
- **Morphological Equivalence:** Equivalent to grayscale erosion with a flat flat structuring element: $g = f \ominus b$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N \times K^2)$ requiring $(K^2 - 1)$ comparisons per pixel.
- **Space Complexity:** $O(M \times N)$ auxiliary storage.

---

## 7. Edge Cases & Boundary Handling
Applying Min filter to dark pepper noise will amplify dark spots; it is strictly intended for bright outlier (salt) suppression.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Monotonic darkening: For all coordinates $(x, y)$, $I_{min}(x, y) \le I(x, y)$.
- Total extinction of isolated salt: Any isolated 255 pixel surrounded by $< 255$ neighbors is reduced to the background level.
