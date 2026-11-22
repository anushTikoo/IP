# Algorithm Guide: Comprehensive Histogram Processing Suite

## 1. Problem Statement & Objective
Unified execution and comparative analysis of Contrast Stretching, Global Histogram Equalization, and Histogram Matching in a single experimental workflow.

---

## 2. Input and Output Specifications
- **Input:** Input test image $I_{src}$ and reference image $I_{tgt}$ with dynamic ranges $[0, 255]$.
- **Output:** Contrast-stretched, Equalized, and Matched image matrices and their corresponding histogram/CDF profiles.

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Load source image and target reference image.
- **Step 2:** Execute Contrast Stretching: $I_{stretch} = \frac{I_{src} - r_{min}}{r_{max} - r_{min}} \times 255$.
- **Step 3:** Execute Histogram Equalization: Compute $CDF_{src}$ and map $I_{eq} = \text{round}(CDF_{src}[I_{src}] \times 255)$.
- **Step 4:** Execute Histogram Matching: Map source CDF into target CDF via inverse nearest-neighbor LUT.
- **Step 5:** Compute histograms and cumulative distributions for all processed outputs.
- **Step 6:** Display multi-panel comparative visual gallery with quantitative histogram metrics.

---

## 4. Structured Pseudocode
```text
ALGORITHM ComprehensiveHistogramProcessing(Image src, Image tgt):
    I_stretch = ContrastStretching(src)
    I_eq      = HistogramEqualization(src)
    I_match   = HistogramMatching(src, tgt)

    PlotComparisonGrid([src, I_stretch, I_eq, I_match, tgt])
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Stretching:** $s = \frac{r - \min}{\max - \min} \times 255$
- **Equalization:** $s = T(r) = (L-1) \cdot CDF(r)$
- **Matching:** $z = G^{-1}(T(r))$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N + L^2)$ linear in image size.
- **Space Complexity:** $O(M \times N)$ auxiliary storage per processed output.

---

## 7. Edge Cases & Boundary Handling
Equalization may cause over-enhancement in images with large background areas, while contrast stretching fails if noise pixels already touch 0 and 255.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Contrast stretching requires $\min > 0$ or $\max < 255$ to produce any change; otherwise $I_{stretch} = I_{src}$.
- Equalization maximizes entropy across the intensity distribution.
