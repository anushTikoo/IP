# Algorithm Guide: Edge Detection using Prewitt Operator

## 1. Problem Statement & Objective
Detect directional spatial intensity discontinuities using 1st-order Prewitt gradient convolution kernels and compute gradient magnitude.

---

## 2. Input and Output Specifications
- **Input:** Grayscale image $I \in \mathbb{R}^{M \times N}$, binarization threshold $T$.
- **Output:** Horizontal gradient $G_x$, vertical gradient $G_y$, gradient magnitude $G$, and binary edge map $E$ (`uint8`).

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Read input image or generate synthetic geometric shapes with sharp step edges.
- **Step 2:** Define $3 \times 3$ Prewitt horizontal kernel $K_x = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]$ and vertical kernel $K_y = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]$.
- **Step 3:** Allocate float64 gradient matrices $G_x, G_y, G$ of size $M \times N$.
- **Step 4:** Convolve interior pixels ($1 \le i < M-1, 1 \le j < N-1$) with $K_x$ to compute $G_x(i, j) = \sum (R \odot K_x)$.
- **Step 5:** Convolve interior pixels with $K_y$ to compute $G_y(i, j) = \sum (R \odot K_y)$.
- **Step 6:** Compute gradient magnitude: $G(i, j) = \sqrt{G_x^2(i, j) + G_y^2(i, j)}$ or $G(i, j) = |G_x(i, j)| + |G_y(i, j)|$.
- **Step 7:** Threshold $G$ at cutoff $T$ to produce binary edge map $E(i, j) = 255$ if $G(i, j) \ge T$ else $0$.
- **Step 8:** Display $G_x, G_y, G$, and binary edge map.

---

## 4. Structured Pseudocode
```text
ALGORITHM PrewittEdgeDetection(Image I, float threshold):
    M, N = dimensions of I
    Kx = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
    Ky = [[-1, -1, -1], [ 0,  0,  0], [ 1,  1,  1]]

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
- **Prewitt Kernels:**

  $$
  K_x = \begin{bmatrix} -1 & 0 & 1 \\ -1 & 0 & 1 \\ -1 & 0 & 1 \end{bmatrix}, \quad K_y = \begin{bmatrix} -1 & -1 & -1 \\ 0 & 0 & 0 \\ 1 & 1 & 1 \end{bmatrix}
  $$
- **Gradient Magnitude:** $|\nabla f| = \sqrt{G_x^2 + G_y^2} \approx |G_x| + |G_y|$
- **Gradient Direction:** $\theta = \arctan\left(\frac{G_y}{G_x}\right)$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N \times 9)$ — fixed 9 multiplications per pixel for each directional kernel.
- **Space Complexity:** $O(M \times N)$ auxiliary storage for gradient matrices.

---

## 7. Edge Cases & Boundary Handling
Unpadded borders ($i=0, M-1$ or $j=0, N-1$) receive $0$ gradient magnitude.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Zero-response on flat regions: Sum of kernel weights is 0 ($\sum K_x = 0, \sum K_y = 0$), so constant intensity regions produce $G=0$.
- Directional orthogonality: $K_x$ responds maximally to vertical edges; $K_y$ responds maximally to horizontal edges.
