# Algorithm Guide: Edge Detection using 2nd-Order Laplacian Operator

## 1. Problem Statement & Objective
Detect edges through second-order spatial derivatives and locate intensity transitions via zero-crossing points in an isotropic (rotation-invariant) manner.

---

## 2. Input and Output Specifications
- **Input:** Grayscale image $I \in \mathbb{R}^{M \times N}$, zero-crossing sensitivity threshold $\tau$.
- **Output:** Laplacian response matrix $L \in \mathbb{R}^{M \times N}$ and binary zero-crossing edge map $E$ (`uint8`).

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Read input grayscale image or synthesize test image.
- **Step 2:** Pre-smooth with Gaussian filter if image contains noise (Laplacian of Gaussian / LoG formulation).
- **Step 3:** Define $3 \times 3$ Laplacian kernel with center $-4$: $K = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]$ or with diagonals $-8$: $K_8 = [[1, 1, 1], [1, -8, 1], [1, 1, 1]]$.
- **Step 4:** Convolve image with Laplacian kernel to obtain 2nd-derivative response matrix $L$ (`float64`).
- **Step 5 [Zero-Crossing Detection]:** For each pixel $(i, j)$, examine opposite neighbor pairs $(L(i-1, j), L(i+1, j))$ and $(L(i, j-1), L(i, j+1))$.
- **Step 6:** If an opposite pair has opposing signs (one $>0$, one $<0$) and $|L_{pos} - L_{neg}| > \tau$, designate $(i, j)$ as an edge pixel ($E(i, j) = 255$).
- **Step 7:** Plot Laplacian response and detected zero-crossing edge map.

---

## 4. Structured Pseudocode
```text
ALGORITHM LaplacianEdgeDetection(Image I, float tau):
    M, N = dimensions of I
    K = [[0,  1, 0],
         [1, -4, 1],
         [0,  1, 0]]

    Initialize L[M, N] as float64
    Initialize Edge[M, N] as uint8

    // 1. Convolution
    FOR i = 1 TO M - 2 DO:
        FOR j = 1 TO N - 2 DO:
            R = I[i-1 : i+2, j-1 : j+2]
            L[i, j] = sum(R * K)
        END FOR
    END FOR

    // 2. Zero-Crossing Detection
    FOR i = 1 TO M - 2 DO:
        FOR j = 1 TO N - 2 DO:
            // Check Vertical and Horizontal opposites
            v_cross = (L[i-1, j] * L[i+1, j] < 0) AND abs(L[i-1, j] - L[i+1, j]) > tau
            h_cross = (L[i, j-1] * L[i, j+1] < 0) AND abs(L[i, j-1] - L[i, j+1]) > tau

            IF v_cross OR h_cross THEN:
                Edge[i, j] = 255
            ELSE:
                Edge[i, j] = 0
            END IF
        END FOR
    END FOR

    RETURN L, Edge
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Continuous Laplacian:** $\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}$
- **Standard 4-Neighbor Discrete Approximation:** $\nabla^2 f(x, y) = f(x+1, y) + f(x-1, y) + f(x, y+1) + f(x, y-1) - 4f(x, y)$
- **8-Neighbor Approximation:** $\nabla^2 f(x, y) = \sum_{s=-1}^1 \sum_{t=-1}^1 f(x+s, y+t) - 8f(x, y)$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N \times 9)$ for convolution plus $O(M \times N)$ for zero-crossing check.
- **Space Complexity:** $O(M \times N)$ auxiliary storage for 2nd derivative float matrix.

---

## 7. Edge Cases & Boundary Handling
Extreme sensitivity to high-frequency noise requires either Gaussian pre-smoothing or a significant zero-crossing threshold $	au$ to prevent false edges.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Isotropy: The Laplacian operator is rotation-invariant (produces identical response regardless of edge orientation).
- Double-edge effect: Laplacian creates a positive spike on the dark side and a negative trough on the light side of a step edge.
