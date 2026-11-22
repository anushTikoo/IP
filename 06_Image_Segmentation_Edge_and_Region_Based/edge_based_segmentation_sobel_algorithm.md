# Algorithm Guide: Edge-Based Image Segmentation using Sobel Gradients

## 1. Problem Statement & Objective
Segment distinct objects from background by extracting gradient magnitude boundaries, applying thresholding, and closing contour gaps to isolate coherent object masks.

---

## 2. Input and Output Specifications
- **Input:** Grayscale image $I \in \mathbb{R}^{M \times N}$, edge threshold $T_{edge}$.
- **Output:** Gradient magnitude $G$, binary edge map $E$, and filled segmented regions $S$ (`uint8`).

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Read input image; apply mild Gaussian pre-smoothing to suppress noise.
- **Step 2:** Convolve with horizontal and vertical Sobel kernels: $G_x = I * K_x$, $G_y = I * K_y$.
- **Step 3:** Compute Euclidean gradient magnitude: $G = \sqrt{G_x^2 + G_y^2}$.
- **Step 4:** Threshold gradient magnitude: $E(i, j) = 255$ if $G(i, j) \ge T_{edge}$ else $0$.
- **Step 5 [Contour Closing]:** Apply morphological closing ($E \bullet B$) using a small $3 \times 3$ disk/box to bridge minor edge discontinuities.
- **Step 6 [Region Filling]:** Apply binary flood fill starting from background corners to fill enclosed interior cavities.
- **Step 7:** Plot original image, gradient magnitude, closed edges, and segmented mask.

---

## 4. Structured Pseudocode
```text
ALGORITHM EdgeBasedSegmentation(Image I, float threshold):
    Smoothed = GaussianBlur(I, kernel_size=3)
    Gx, Gy   = SobelGradients(Smoothed)
    G_mag    = sqrt(Gx^2 + Gy^2)

    // Edge Thresholding
    EdgeMap = (G_mag >= threshold) * 255

    // Morphological Gap Closing
    ClosedEdges = MorphologicalClosing(EdgeMap, Kernel3x3)

    // Cavity Filling
    SegmentedMask = BinaryFillHoles(ClosedEdges)

    RETURN G_mag, EdgeMap, SegmentedMask
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Sobel Magnitude:** $G(x, y) = \sqrt{\left(\frac{\partial f}{\partial x}\right)^2 + \left(\frac{\partial f}{\partial y}\right)^2}$
- **Binarization:**

  $$
  E(x, y) = \begin{cases}
    255 & \text{if } G(x, y) \ge T \\
    0 & \text{otherwise}
  \end{cases}
  $$
- **Morphological Closing:** $E_{closed} = (E \oplus B) \ominus B$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N)$ linear in pixel count across convolution, thresholding, and morphological closing.
- **Space Complexity:** $O(M \times N)$ auxiliary storage for edge maps and masks.

---

## 7. Edge Cases & Boundary Handling
Broken/leaky edges: If edge detection leaves a single-pixel gap that morphological closing cannot bridge, hole-filling will leak across the boundary into the background.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Edge-region duality: True region boundaries must coincide with localized peaks in gradient magnitude.
- Binarization compactness: Segmented regions are represented as binary masks $\{0, 255\}$.
