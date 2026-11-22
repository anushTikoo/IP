# Algorithm Guide: Comprehensive Image Segmentation: Global Thresholding, Edge-Based, and Region-Based

## 1. Problem Statement & Objective
Implement and contrast the three fundamental paradigms of digital image segmentation: Global Otsu Thresholding, Sobel Edge-Based Contour Closing, and Seeded Region Growing.

---

## 2. Input and Output Specifications
- **Input:** Grayscale image $I \in \mathbb{R}^{M \times N}$.
- **Output:** Segmented binary masks for Otsu ($S_{otsu}$), Edge-Based ($S_{edge}$), and Region-Growing ($S_{region}$) methods.

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Load input grayscale image; display original intensity distribution.
- **Step 2 [Otsu's Thresholding]:** Calculate between-class variance $\sigma_B^2(T)$ across all $T \in [0, 255]$; select $T^*$ maximizing $\sigma_B^2$. Create binary mask $S_{otsu} = (I \ge T^*) \times 255$.
- **Step 3 [Edge-Based]:** Convolve with Sobel kernels, compute magnitude $G$, threshold at edge cutoff, and close gaps using morphology to produce $S_{edge}$.
- **Step 4 [Region-Growing]:** Select seed point inside target object; perform breadth-first region growth using intensity tolerance $T_{sim}$ to produce $S_{region}$.
- **Step 5:** Compute comparative metrics (Jaccard similarity, boundary smoothness, connected component count).
- **Step 6:** Display multi-panel comparative figure.

---

## 4. Structured Pseudocode
```text
ALGORITHM ComprehensiveSegmentation(Image I):
    // 1. Otsu Thresholding
    T_otsu = OtsuOptimalThreshold(I)
    S_otsu = (I >= T_otsu) * 255

    // 2. Edge-Based Segmentation
    G_mag  = SobelMagnitude(I)
    S_edge = BinaryFillHoles(MorphologicalClosing(G_mag >= 50))

    // 3. Region-Based Segmentation
    seed   = FindCentroidSeed(S_otsu)
    S_reg  = RegionGrowing(I, seed, threshold=20)

    DisplayComparisonGrid([I, S_otsu, S_edge, S_reg])
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Otsu's Between-Class Variance:** $\sigma_B^2(T) = \omega_0(T) \omega_1(T) [\mu_0(T) - \mu_1(T)]^2$
- **Optimal Threshold:** $T^* = \arg\max_{0 \le T < L} \sigma_B^2(T)$
- **Partitioning Constraint:** $\bigcup_{i=1}^n R_i = I, \quad R_i \cap R_j = \emptyset \quad (i \neq j)$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N + L)$ for Otsu + $O(M \times N)$ for Edge/Region growing.
- **Space Complexity:** $O(M \times N)$ auxiliary storage per segmentation mask.

---

## 7. Edge Cases & Boundary Handling
Non-uniform illumination (vignetting, shadowing) causes Otsu thresholding to fail, whereas localized Region Growing remains robust.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Completeness: Image pixels are partitioned into binary disjoint sets (foreground vs background).
- Complementary strengths: Edge-based finds high-contrast boundaries; Region-based groups uniform interior textures.
