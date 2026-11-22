# Algorithm Guide: Morphological Erosion and Dilation

## 1. Problem Statement & Objective
Perform fundamental set-theoretic morphological operations (Erosion and Dilation) on binary images using custom structuring elements.

---

## 2. Input and Output Specifications
- **Input:** Binary image $I \in \{0, 1\}^{M \times N}$, Structuring Element $B \in \{0, 1\}^{K \times K}$ (e.g. $3 \times 3$ cross or square).
- **Output:** Eroded image $I_{eroded}$ and Dilated image $I_{dilated}$ (`uint8` binary masks with values in $\{0, 255\}$).

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Read input binary image or threshold grayscale image at cutoff 128 to create binary matrix $A$.
- **Step 2:** Define $3 \times 3$ flat structuring element $B$ with origin at its center $(1, 1)$.
- **Step 3:** Allocate output matrices $I_{eroded}$ and $I_{dilated}$ initialized to 0.
- **Step 4 [Erosion]:** For each coordinate $(i, j)$ in interior bounds: translate $B$ to $(i, j)$. If all foreground positions of $B$ coincide with foreground pixels of $A$ ($B_{(i, j)} \subseteq A$), assign $I_{eroded}(i, j) = 255$; otherwise $0$.
- **Step 5 [Dilation]:** For each coordinate $(i, j)$ in interior bounds: reflect and translate $B$ to $(i, j)$. If at least one foreground pixel of translated $B$ overlaps foreground of $A$ ($(\hat{B})_{(i, j)} \cap A \neq \emptyset$), assign $I_{dilated}(i, j) = 255$; otherwise $0$.
- **Step 6:** Display original, eroded, and dilated images side-by-side.

---

## 4. Structured Pseudocode
```text
ALGORITHM MorphologicalErosionDilation(BinaryImage A, SE B):
    M, N = dimensions of A
    k_rows, k_cols = dimensions of B
    r = k_rows // 2, c = k_cols // 2

    Initialize Eroded[M, N] as 0
    Initialize Dilated[M, N] as 0

    // 1. Erosion: All 1s in B must match 1s in window
    FOR i = r TO M - 1 - r DO:
        FOR j = c TO N - 1 - c DO:
            window = A[i - r : i + r + 1, j - c : j + c + 1]
            IF all(window[B == 1] == 1) THEN:
                Eroded[i, j] = 255
            END IF
        END FOR
    END FOR

    // 2. Dilation: At least one overlap with B
    FOR i = r TO M - 1 - r DO:
        FOR j = c TO N - 1 - c DO:
            window = A[i - r : i + r + 1, j - c : j + c + 1]
            IF any(window[B == 1] == 1) THEN:
                Dilated[i, j] = 255
            END IF
        END FOR
    END FOR

    RETURN Eroded, Dilated
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Erosion:** $A \ominus B = \{ z \mid (B)_z \subseteq A \}$
- **Dilation:** $A \oplus B = \{ z \mid (\hat{B})_z \cap A \neq \emptyset \}$
- **Duality Principle:** $(A \ominus B)^c = A^c \oplus \hat{B}$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N \times K^2)$ comparisons across image grid.
- **Space Complexity:** $O(M \times N)$ auxiliary storage for binary output matrices.

---

## 7. Edge Cases & Boundary Handling
Structuring elements extending outside image boundary require border padding (pad with 0 for dilation, pad with 1 or crop for erosion).

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Subset inclusion: Erosion is an anti-extensive operation on foreground: $(A \ominus B) \subseteq A \subseteq (A \oplus B)$.
- Dilation fills internal voids and holes smaller than $B$, whereas erosion removes foreground islands smaller than $B$.
