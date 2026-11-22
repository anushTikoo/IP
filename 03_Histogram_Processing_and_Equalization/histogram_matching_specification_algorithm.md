# Algorithm Guide: Histogram Matching (Specification)

## 1. Problem Statement & Objective
Transform the intensity distribution of a Source image so that its histogram and subjective appearance match a specified Target reference image.

---

## 2. Input and Output Specifications
- **Input:** Source image $I_{src} \in \mathbb{R}^{M_1 \times N_1}$ and Target reference image $I_{tgt} \in \mathbb{R}^{M_2 \times N_2}$.
- **Output:** Matched image $I_{matched} \in \mathbb{R}^{M_1 \times N_1}$ (`uint8`) and inverse mapping Look-Up Table.

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Read source and target images, or synthesize a dark source image and a high-key target image.
- **Step 2:** Compute normalized histogram and CDF of source image: $CDF_{src}[s] = \frac{1}{M_1 N_1} \sum_{i=0}^s H_{src}[i]$.
- **Step 3:** Compute normalized histogram and CDF of target image: $CDF_{tgt}[z] = \frac{1}{M_2 N_2} \sum_{j=0}^z H_{tgt}[j]$.
- **Step 4 [Discrete Inverse Mapping]:** Initialize lookup table $LUT$ of size 256. For each source intensity $s \in [0, 255]$, find target intensity $z \in [0, 255]$ that minimizes absolute CDF error: $LUT[s] = \arg\min_z |CDF_{src}[s] - CDF_{tgt}[z]|$.
- **Step 5:** Apply LUT to source image: $I_{matched} = LUT[I_{src}]$.
- **Step 6:** Render source, target, and matched images alongside their respective histograms and CDF curves.

---

## 4. Structured Pseudocode
```text
ALGORITHM HistogramMatching(Image src, Image tgt):
    // 1. Compute Normalized CDFs
    cdf_src = ComputeNormalizedCDF(src)
    cdf_tgt = ComputeNormalizedCDF(tgt)

    // 2. Build Inverse Mapping LUT
    Initialize LUT[256] as uint8
    FOR s = 0 TO 255 DO:
        min_diff = infinity
        best_z = 0
        FOR z = 0 TO 255 DO:
            diff = abs(cdf_src[s] - cdf_tgt[z])
            IF diff < min_diff THEN:
                min_diff = diff
                best_z = z
            END IF
        END FOR
        LUT[s] = best_z
    END FOR

    // 3. Map Source Image
    Matched = LUT[src]
    RETURN Matched, LUT
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Forward Equalization Transformations:** $s = T(r) = \int_0^r p_r(w) dw$, \quad $v = G(z) = \int_0^z p_z(w) dw$
- **Inverse Transformation:** $z = G^{-1}(s) = G^{-1}(T(r))$
- **Discrete Nearest-Neighbor Search:** $z^* = \arg\min_{z \in [0, 255]} |CDF_{src}(s) - CDF_{tgt}(z)|$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M_1 N_1 + M_2 N_2 + L^2)$ where $L=256$ ($L^2 = 65,536$ comparisons, executing in $< 1$ ms).
- **Space Complexity:** $O(M_1 N_1 + L)$ memory.

---

## 7. Edge Cases & Boundary Handling
When multiple target levels $z$ produce the same minimum difference, selecting the smallest index (leftmost nearest neighbor) guarantees deterministic behavior.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- CDF Range matching: Both source and target CDFs are normalized to $[0.0, 1.0]$, ensuring valid distance minimization.
- Shape transfer: The cumulative distribution of the matched output closely approximates $CDF_{tgt}$.
