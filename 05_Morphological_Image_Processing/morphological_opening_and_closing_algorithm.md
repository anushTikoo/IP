# Algorithm Guide: Morphological Opening and Closing

## 1. Problem Statement & Objective
Perform compound morphological filtering: Opening (Erosion followed by Dilation) to smooth contours and eliminate small protrusions, and Closing (Dilation followed by Erosion) to bridge narrow breaks and fill small holes.

---

## 2. Input and Output Specifications
- **Input:** Binary image $I \in \{0, 1\}^{M \times N}$, Structuring Element $B$.
- **Output:** Opened image $I_{open}$ and Closed image $I_{close}$ (`uint8`).

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Read input binary image or threshold noisy image containing background specks and foreground holes.
- **Step 2:** Define $3 \times 3$ structuring element $B$.
- **Step 3 [Opening]:** First execute Erosion on $A$ with $B$: $A_1 = A \ominus B$. Then execute Dilation on $A_1$ with $B$: $I_{open} = A_1 \oplus B$.
- **Step 4 [Closing]:** First execute Dilation on $A$ with $B$: $A_2 = A \oplus B$. Then execute Erosion on $A_2$ with $B$: $I_{close} = A_2 \ominus B$.
- **Step 5:** Render input, opened, and closed images.

---

## 4. Structured Pseudocode
```text
ALGORITHM MorphologicalOpeningClosing(BinaryImage A, SE B):
    // 1. Opening: Erosion followed by Dilation
    A_eroded = MorphologicalErosion(A, B)
    Opened   = MorphologicalDilation(A_eroded, B)

    // 2. Closing: Dilation followed by Erosion
    A_dilated = MorphologicalDilation(A, B)
    Closed    = MorphologicalErosion(A_dilated, B)

    RETURN Opened, Closed
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Opening:** $A \circ B = (A \ominus B) \oplus B$
- **Closing:** $A \bullet B = (A \oplus B) \ominus B$
- **Idempotence Property:** $(A \circ B) \circ B = A \circ B$ and $(A \bullet B) \bullet B = A \bullet B$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N \times K^2)$ — two sequential morphological passes per operation.
- **Space Complexity:** $O(M \times N)$ intermediate and final buffer storage.

---

## 7. Edge Cases & Boundary Handling
Structuring element dimensions must be smaller than primary foreground features to avoid completely annihilating target structures during initial erosion in Opening.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Anti-extensivity of Opening: $(A \circ B) \subseteq A$.
- Extensivity of Closing: $A \subseteq (A \bullet B)$.
- Area preservation: Unlike standalone erosion or dilation, opening and closing preserve the global scale and dimensions of the object.
