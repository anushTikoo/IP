# Algorithm Guide: Edge Detection using Sobel Operator

## 1. Problem Statement & Objective
Detect intensity edges using central-difference weighting that combines differentiation with local Gaussian-like smoothing for enhanced noise resistance.

---

## 2. Input and Output Specifications
- **Input:** Grayscale image $I \in \mathbb{R}^{M \times N}$, binarization threshold $T$.
- **Output:** Sobel horizontal gradient $G_x$, vertical gradient $G_y$, gradient magnitude $G$, gradient direction $\theta$, and binary edge map $E$.

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Read input grayscale image or generate synthetic noisy test pattern.
- **Step 2:** Define $3 \times 3$ Sobel kernels with center weight 2: $K_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]$ and $K_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]$.
- **Step 3:** Allocate float64 arrays $G_x, G_y, G, \theta$ of dimensions $M \times N$.
- **Step 4:** Slide $3 \times 3$ window over interior pixels ($1 \le i < M-1, 1 \le j < N-1$): compute $G_x(i, j) = \sum (R \odot K_x)$ and $G_y(i, j) = \sum (R \odot K_y)$.
- **Step 5:** Compute Euclidean gradient magnitude: $G(i, j) = \sqrt{G_x^2(i, j) + G_y^2(i, j)}$.
- **Step 6:** Compute edge orientation angle: $\theta(i, j) = \arctan2(G_y(i, j), G_x(i, j)) \times \frac{180}{\pi}$.
- **Step 7:** Threshold $G$ at value $T$ to generate binary edge map $E$.
- **Step 8:** Plot $G_x, G_y$, magnitude $G$, and thresholded edge map.

---

## 4. Structured Pseudocode
```text
ALGORITHM SobelEdgeDetection(Image I, float threshold):
    M, N = dimensions of I
    Kx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    Ky = [[-1, -2, -1], [ 0,  0,  0], [ 1,  2,  1]]

    Initialize Gx[M, N], Gy[M, N], G[M, N] as float64
    Initialize Edge[M, N] as uint8

    FOR i = 1 TO M - 2 DO:
        FOR j = 1 TO N - 2 DO:
            R = I[i-1 : i+2, j-1 : j+2]
            Gx[i, j] = sum(R * Kx)
            Gy[i, j] = sum(R * Ky)
            G[i, j]  = sqrt(Gx[i, j]^2 + Gy[i, j]^2)
            
            IF G[i, j] >= threshold THEN:
                Edge[i, j] = 255
            ELSE:
                Edge[i, j] = 0
            END IF
        END FOR
    END FOR

    RETURN Gx, Gy, G, Edge
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Sobel Kernels:** $K_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}, \quad K_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}$
- **Separable Kernel Decomposition:** $K_x = \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix} \begin{bmatrix} -1 & 0 & 1 \end{bmatrix}, \quad K_y = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix} \begin{bmatrix} 1 & 2 & 1 \end{bmatrix}$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N \times 9)$ — 9 multiply-adds per pixel per kernel.
- **Space Complexity:** $O(M \times N)$ auxiliary memory for gradients.

---

## 7. Edge Cases & Boundary Handling
When computing gradient orientation, division by zero ($G_x = 0$) is safely avoided by using `arctan2(Gy, Gx)`.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Kernel symmetry: Center weighting of 2 provides maximum noise smoothing along the axis perpendicular to differentiation.
- Zero sum: Sum of all weights in $K_x$ and $K_y$ equals zero, giving zero response in uniform illumination.
