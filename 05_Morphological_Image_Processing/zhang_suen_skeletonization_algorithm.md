# Algorithm Guide: Zhang-Suen Thinning and Skeletonization

## 1. Problem Statement & Objective
Iteratively erode the boundaries of connected binary foreground shapes down to a 1-pixel-wide medial axis skeleton while strictly preserving topological connectivity and endpoints.

---

## 2. Input and Output Specifications
- **Input:** Binary image $I \in \{0, 1\}^{M \times N}$ where foreground is 1 and background is 0.
- **Output:** 1-pixel-wide Skeleton image $I_{skel} \in \{0, 255\}^{M \times N}$ (`uint8`).

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Convert input to binary matrix $A$ where foreground $= 1$ and background $= 0$.
- **Step 2:** Loop until no pixels are deleted in a full cycle:
- **Step 3 [Sub-iteration 1]:** Scan all pixels $(i, j)$ with $A(i, j) == 1$. Extract 8-neighborhood ordered clockwise: $(P_2, P_3, P_4, P_5, P_6, P_7, P_8, P_9)$. Mark $(i, j)$ for deletion if: (a) $2 \le B(P_1) \le 6$, (b) $A(P_1) = 1$, (c) $P_2 \cdot P_4 \cdot P_6 = 0$, (d) $P_4 \cdot P_6 \cdot P_8 = 0$.
- **Step 4:** Set all marked pixels in Sub-iteration 1 to 0 simultaneously.
- **Step 5 [Sub-iteration 2]:** Scan all remaining pixels $(i, j)$ with $A(i, j) == 1$. Mark $(i, j)$ for deletion if: (a) $2 \le B(P_1) \le 6$, (b) $A(P_1) = 1$, (c) $P_2 \cdot P_4 \cdot P_8 = 0$, (d) $P_2 \cdot P_6 \cdot P_8 = 0$.
- **Step 6:** Set all marked pixels in Sub-iteration 2 to 0 simultaneously.
- **Step 7:** If the union of pixels deleted in both sub-iterations is 0, terminate; else repeat.
- **Step 8:** Scale remaining skeleton pixels to 255 and render.

---

## 4. Structured Pseudocode
```text
ALGORITHM ZhangSuenThinning(BinaryImage img):
    A = copy(img)
    changed = True

    WHILE changed DO:
        changed = False
        markers = []

        // Sub-iteration 1
        FOR i = 1 TO M - 2 DO:
            FOR j = 1 TO N - 2 DO:
                IF A[i, j] == 1 THEN:
                    P2, P3, P4, P5, P6, P7, P8, P9 = GetNeighbors(A, i, j)
                    B = sum([P2, P3, P4, P5, P6, P7, P8, P9])
                    A_trans = CountTransitions([P2, P3, P4, P5, P6, P7, P8, P9, P2])

                    IF 2 <= B <= 6 AND A_trans == 1 THEN:
                        IF P2 * P4 * P6 == 0 AND P4 * P6 * P8 == 0 THEN:
                            markers.append((i, j))
                        END IF
                    END IF
                END IF
            END FOR
        END FOR
        IF markers IS NOT EMPTY THEN changed = True
        FOR (r, c) IN markers DO A[r, c] = 0

        // Sub-iteration 2
        markers = []
        FOR i = 1 TO M - 2 DO:
            FOR j = 1 TO N - 2 DO:
                IF A[i, j] == 1 THEN:
                    P2, P3, P4, P5, P6, P7, P8, P9 = GetNeighbors(A, i, j)
                    B = sum([P2, P3, P4, P5, P6, P7, P8, P9])
                    A_trans = CountTransitions([P2, P3, P4, P5, P6, P7, P8, P9, P2])

                    IF 2 <= B <= 6 AND A_trans == 1 THEN:
                        IF P2 * P4 * P8 == 0 AND P2 * P6 * P8 == 0 THEN:
                            markers.append((i, j))
                        END IF
                    END IF
                END IF
            END FOR
        END FOR
        IF markers IS NOT EMPTY THEN changed = True
        FOR (r, c) IN markers DO A[r, c] = 0
    END WHILE

    RETURN A * 255
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Neighbor Count:** $B(P_1) = \sum_{k=2}^9 P_k$
- **0-to-1 Transitions:** $A(P_1) = \sum_{k=2}^9 \mathbb{I}(P_k = 0 \text{ and } P_{k+1} = 1) \text{ with } P_{10} = P_2$
- **Sub-iteration 1 Directional Conditions:** $P_2 \cdot P_4 \cdot P_6 = 0 \quad \text{and} \quad P_4 \cdot P_6 \cdot P_8 = 0$
- **Sub-iteration 2 Directional Conditions:** $P_2 \cdot P_4 \cdot P_8 = 0 \quad \text{and} \quad P_2 \cdot P_6 \cdot P_8 = 0$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(k \cdot M \cdot N)$ where $k$ is half the maximum stroke thickness of the thickest object.
- **Space Complexity:** $O(M \times N)$ auxiliary storage for the deletion marker list and working array.

---

## 7. Edge Cases & Boundary Handling
If a line is only 1-pixel thick, $B(P_1) < 2$ or $A(P_1) 
eq 1$ protects it from being deleted, preventing stroke erasure.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Topology preservation: Number of connected components and Euler number ($\chi = C - H$) remain strictly invariant.
- 1-pixel width: Upon convergence, all lines are guaranteed to have stroke width of exactly 1 pixel.
