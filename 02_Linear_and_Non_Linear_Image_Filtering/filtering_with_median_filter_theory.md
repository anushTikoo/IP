# Viva & Theory Guide: Median Filtering

## 1. First-Principles Analogy
> Imagine an Olympic diving competition where one biased judge gives an absurd score of 0 and another gives 10. If the judges take an average, those two extreme outliers wreck the final score. But if they take the **median** (the middle score after sorting), the two outliers are completely ignored, reflecting the true consensus of the remaining judges.

---

## 2. What It Is (Concept & Definition)
- **Median Filter**: A non-linear spatial order-statistic (rank-order) filter that replaces the center pixel of a sliding window with the mathematical median of all pixel intensities inside that window.
- **Classification**: Non-linear neighborhood operation. It cannot be expressed as a linear matrix convolution kernel because the median operation violates the principle of superposition:

  $$
  \text{Median}(f_1 + f_2) \neq \text{Median}(f_1) + \text{Median}(f_2)
  $$

---

## 3. Why We Do It (Motivation & Practical Use Cases)
- **Removal of Impulse / Salt-and-Pepper Noise**: Caused by malfunctioning pixel bits in CCD/CMOS sensors, analog-to-digital converter bit transmission errors, or dust on scanner glass.
- **Superior Edge Preservation**: Unlike mean filters which blur sharp step edges, a median filter preserves sharp monotonic transitions (edges) as long as the edge occupies more than half of the neighborhood window ($> k^2 / 2$ pixels).
- **Failure Cases**: Can erode thin lines, sharp isolated corners, and fine textures whose area is smaller than $(k^2 + 1) / 2$.

---

## 4. How It Works (Algorithmic & Mathematical Breakdown)

### A. Mathematical Procedure
For a window $W$ of size $n = k \times k$ (where $k$ is odd, e.g., $3, 5, 7$):
1. Extract all pixel values in the local neighborhood centered at $(x, y)$:

   $$
   \{p_1, p_2, \dots, p_n\}
   $$
2. Sort the values in ascending numerical order:

   $$
   p_{(1)} \le p_{(2)} \le \dots \le p_{\left(\frac{n+1}{2}\right)} \le \dots \le p_{(n)}
   $$
3. Assign the median value (the rank $\frac{n+1}{2}$ element) to the output pixel:

   $$
   g(x, y) = p_{\left(\frac{n+1}{2}\right)}
   $$

### B. Impulse Noise Removal Example
Consider a $3 \times 3$ neighborhood with a corrupted white "salt" pixel ($255$) on a dark gray surface ($50$):
$$
\begin{bmatrix} 52 & 50 & 51 \\ 49 & \mathbf{255} & 53 \\ 50 & 51 & 48 \end{bmatrix}
$$
1. Flatten and sort: $[48, 49, 50, 50, \mathbf{51}, 51, 52, 53, 255]$
2. 5th element (median) = **51**.
3. Output pixel is replaced with $51$. The $255$ outlier is completely wiped out without leaving a trace!

### C. Computational Complexity
- Naive sorting per window: $O(k^2 \log(k^2))$.
- Huang's fast median algorithm: Maintains a running local 256-bin histogram as the window shifts horizontally, updating only by adding the incoming column and subtracting the outgoing column. Complexity drops to $O(k)$ per pixel, independent of window area!

---

## 5. Code Walkthrough & Working

In [`filtering_with_median_filter.py`](file:///home/anushtikoo/Downloads/IP/02_Linear_and_Non_Linear_Image_Filtering/filtering_with_median_filter.py):
- **Cell 1**: Imports `numpy` and `matplotlib.pyplot`.
- **Cell 2**: Creates synthetic test image and injects Salt-and-Pepper noise:
  - Randomly selects $5\%$ of pixels and sets them to $255$ (salt).
  - Randomly selects another $5\%$ and sets them to $0$ (pepper).
- **Cell 3**: First-principles median filter loop:
  - Loops over valid interior pixels $(1 \le i < H-1, 1 \le j < W-1)$.
  - Slices window: `region = img[i-1:i+2, j-1:j+2]`.
  - Computes `np.median(region)` and assigns to `median_img[i, j]`.
- **Cell 4**: Compares the corrupted Salt & Pepper image against the restored Median Filtered result.

---

## 6. High-Yield Viva Questions & Examiner Traps

### Q1: Why is the median filter classified as non-linear?
**Answer**: A system $T$ is linear if and only if it satisfies both **additivity** ($T(f_1 + f_2) = T(f_1) + T(f_2)$) and **homogeneity** ($T(af) = aT(f)$). The median operation fails additivity. For example:
- Let $A = [0, 0, 100] \implies \text{median}(A) = 0$.
- Let $B = [100, 0, 0] \implies \text{median}(B) = 0$.
- Sum $A + B = [100, 0, 100] \implies \text{median}(A + B) = 100$.
- However, $\text{median}(A) + \text{median}(B) = 0 + 0 = 0 \neq 100$. Thus, it is strictly non-linear.

### Q2: What is the maximum density of salt-and-pepper noise a standard $3 \times 3$ median filter can clean?
**Answer**: Since a $3 \times 3$ window contains 9 pixels, the median is the 5th element. If noise occupies $\ge 5$ of the 9 pixels ($> 50\%$ local noise density), the median value itself will be an impulse ($0$ or $255$), causing the filter to fail. To handle noise densities $> 50\%$, an **Adaptive Median Filter** is required, which dynamically expands the window size until a non-noise median is found.

### Q3: Why does a median filter preserve step edges better than a mean filter?
**Answer**: Consider a clean vertical edge where the left 6 pixels are $10$ and the right 3 pixels are $200$: $[10, 10, 10, 10, 10, 10, 200, 200, 200]$.
- Mean filter output: $(60 + 600)/9 = 73.3$ (the sharp jump is blurred).
- Median filter output: sorted array has $10$ at index 5. The output remains $10$! The transition stays sharp and unmoved.
