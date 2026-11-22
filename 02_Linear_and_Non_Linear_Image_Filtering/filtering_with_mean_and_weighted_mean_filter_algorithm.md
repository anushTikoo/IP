# Algorithm Guide: Filtering with Mean (Box) and Weighted Mean Filters

## 1. Problem Statement & Objective
Perform 2D spatial smoothing to suppress high-frequency additive Gaussian noise using uniform Box averaging and distance-weighted Gaussian kernel convolution.

---

## 2. Input and Output Specifications
- **Input:** Grayscale image $I \in \mathbb{R}^{M \times N}$, kernel size $K = 3$, weighted kernel $W \in \mathbb{R}^{3 \times 3}$.
- **Output:** Filtered images $I_{mean}, I_{weighted} \in \mathbb{R}^{M \times N}$ (`uint8`).

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Read input grayscale image or generate synthetic image with synthetic Gaussian noise.
- **Step 2:** Define $3 \times 3$ Box kernel with sum $= 9$ and weighted Gaussian-like kernel $W = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]$ with sum $= 16$.
- **Step 3:** Allocate output arrays $I_{mean}$ and $I_{weighted}$ of size $M \times N$ with zeros (`uint8`).
- **Step 4:** Iterate over interior pixels $(i, j)$ where $1 \le i < M - 1$ and $1 \le j < N - 1$.
- **Step 5:** Extract the $3 \times 3$ local neighborhood: $R = I[i-1:i+2, j-1:j+2]$.
- **Step 6:** Compute Box Mean: $I_{mean}(i, j) = \text{round}(\sum R / 9)$.
- **Step 7:** Compute Weighted Mean: $I_{weighted}(i, j) = \text{round}(\sum (R \odot W) / 16)$.
- **Step 8:** Replicate or zero boundary borders; render comparative results.

---

## 4. Structured Pseudocode
```text
ALGORITHM MeanAndWeightedFilter(Image I, Kernel W):
    M, N = dimensions of I
    Initialize MeanImg[M, N], WeightedImg[M, N] as uint8
    w_sum = sum(W)

    FOR i = 1 TO M - 2 DO:
        FOR j = 1 TO N - 2 DO:
            region = I[i-1 : i+2, j-1 : j+2]
            
            // Box filter (equal weights)
            MeanImg[i, j] = int(sum(region) / 9)
            
            // Weighted filter (element-wise multiplication)
            WeightedImg[i, j] = int(sum(region * W) / w_sum)
        END FOR
    END FOR

    RETURN MeanImg, WeightedImg
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Discrete 2D Convolution:** $g(x, y) = \sum_{s=-a}^a \sum_{t=-b}^b w(s, t) f(x+s, y+t)$
- **Box Kernel ($3 \times 3$):** $K_{box} = \frac{1}{9} \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$
- **Weighted Kernel:** $W = \frac{1}{16} \begin{bmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1 \end{bmatrix}$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N \times K^2)$ where $K=3$ (9 multiplications/additions per pixel).
- **Space Complexity:** $O(M \times N)$ auxiliary storage for the filtered images.

---

## 7. Edge Cases & Boundary Handling
Pixels at borders ($i=0, M-1$ or $j=0, N-1$) lack complete $3 	imes 3$ neighborhoods; handled by boundary zeroing or zero padding.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Energy preservation: Kernel weights sum to exactly $1.0$ ($\sum w_{st} = 1$), ensuring DC illumination of uniform regions is unchanged.
- Low-pass smoothing: High spatial frequencies (sharp edges, noise) are attenuated while low frequencies (flat regions) pass intact.
