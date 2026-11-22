# Algorithm Guide: Morphological Boundary Extraction

## 1. Problem Statement & Objective
Extract exact 1-pixel-wide internal, external, and morphological gradient object boundaries using set difference operations.

---

## 2. Input and Output Specifications
- **Input:** Binary image $I \in \{0, 1\}^{M \times N}$, $3 \times 3$ Structuring Element $B$.
- **Output:** Internal boundary $\beta_{int}$, External boundary $\beta_{ext}$, and Morphological Gradient $G_{morph}$ (`uint8`).

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Read or synthesize binary shapes.
- **Step 2:** Erode image $A$ by structuring element $B$: $A_{eroded} = A \ominus B$.
- **Step 3:** Dilate image $A$ by structuring element $B$: $A_{dilated} = A \oplus B$.
- **Step 4 [Internal Boundary]:** Subtract eroded image from original image: $\beta_{int} = A - A_{eroded}$.
- **Step 5 [External Boundary]:** Subtract original image from dilated image: $\beta_{ext} = A_{dilated} - A$.
- **Step 6 [Morphological Gradient]:** Subtract eroded image from dilated image: $G_{morph} = A_{dilated} - A_{eroded}$.
- **Step 7:** Plot original image and all three extracted boundaries.

---

## 4. Structured Pseudocode
```text
ALGORITHM BoundaryExtraction(BinaryImage A, SE B):
    A_eroded  = MorphologicalErosion(A, B)
    A_dilated = MorphologicalDilation(A, B)

    Beta_internal = A - A_eroded
    Beta_external = A_dilated - A
    Morph_grad    = A_dilated - A_eroded

    RETURN Beta_internal, Beta_external, Morph_grad
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Internal Boundary:** $\beta(A) = A - (A \ominus B)$
- **External Boundary:** $\beta_{ext}(A) = (A \oplus B) - A$
- **Morphological Gradient (Thick Boundary):** $G_{morph}(A) = (A \oplus B) - (A \ominus B) = \beta_{int}(A) \cup \beta_{ext}(A)$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N \times K^2)$ for morphological passes + $O(M \times N)$ for array subtraction.
- **Space Complexity:** $O(M \times N)$ auxiliary storage for boundary maps.

---

## 7. Edge Cases & Boundary Handling
Thin 1-pixel lines completely erode to 0; their internal boundary is the line itself ($A - 0 = A$).

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Boundary thickness: For a $3 \times 3$ structuring element, internal and external boundaries are exactly 1 pixel thick; morphological gradient is 2 pixels thick.
- Disjointness: $\beta_{int} \cap \beta_{ext} = \emptyset$ (internal boundary lies strictly inside $A$, external boundary lies strictly outside $A$).
