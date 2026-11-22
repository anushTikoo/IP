# Algorithm Guide: Filtering with Non-Linear Median Filter

## 1. Problem Statement & Objective
Suppress impulse (Salt-and-Pepper) noise while preserving sharp geometric edges using local rank-order median statistics.

---

## 2. Input and Output Specifications
- **Input:** Grayscale image $I \in \mathbb{R}^{M \times N}$ contaminated with impulse noise, window size $K = 3$.
- **Output:** Denoised image $I_{median} \in \mathbb{R}^{M \times N}$ (`uint8`).

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Acquire input grayscale image or contaminate clean image with synthetic Salt-and-Pepper noise ($0$ and $255$).
- **Step 2:** Allocate output array $I_{median}$ of size $M \times N$ initialized to 0.
- **Step 3:** Iterate through all non-boundary pixels: $1 \le i < M - 1$ and $1 \le j < N - 1$.
- **Step 4:** Extract the $3 \times 3$ neighborhood matrix: $R = I[i-1:i+2, j-1:j+2]$.
- **Step 5:** Flatten $R$ into a 1D vector of 9 elements and sort in ascending order.
- **Step 6:** Select the median element (index $\lfloor 9/2 \rfloor = 4$): $I_{median}(i, j) = R_{sorted}[4]$.
- **Step 7:** Plot noisy image alongside median-filtered output.

---

## 4. Structured Pseudocode
```text
ALGORITHM MedianFilter(Image I, int window_size):
    M, N = dimensions of I
    r = window_size // 2
    Initialize Out[M, N] as uint8

    FOR i = r TO M - 1 - r DO:
        FOR j = r TO N - 1 - r DO:
            window = I[i - r : i + r + 1, j - r : j + r + 1]
            flat_sorted = sort(flatten(window))
            median_val = flat_sorted[len(flat_sorted) // 2]
            Out[i, j] = median_val
        END FOR
    END FOR

    RETURN Out
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Order Statistic Formulation:** $g(x, y) = \text{median}\{ f(x+s, y+t) \mid (s, t) \in W \}$
- **Rank Selection:** For $k = 2m+1$ elements: $R_{(1)} \le R_{(2)} \le \dots \le R_{(m+1)} \le \dots \le R_{(2m+1)}$, where $\text{median} = R_{(m+1)}$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N \times K^2 \log(K^2))$ due to sorting $K^2$ elements per pixel.
- **Space Complexity:** $O(M \times N)$ auxiliary storage for output image.

---

## 7. Edge Cases & Boundary Handling
Windows overlapping corners/borders are restricted to interior coordinates $1 \le i < M-1, 1 \le j < N-1$ to prevent out-of-bounds indexing.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Impulse immunity: Outlier spikes ($0$ or $255$) occupy extreme ends of sorted vector and are never selected as the median.
- Edge preservation: Step edges with $\ge 50\%$ majority support are reproduced sharply without blurring.
