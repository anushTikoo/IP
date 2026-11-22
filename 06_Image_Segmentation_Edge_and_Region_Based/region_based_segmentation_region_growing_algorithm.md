# Algorithm Guide: Region-Based Segmentation using Region Growing

## 1. Problem Statement & Objective
Segment homogeneous connected object regions by iteratively appending neighboring pixels to seed points based on intensity similarity criteria.

---

## 2. Input and Output Specifications
- **Input:** Grayscale image $I \in \mathbb{R}^{M \times N}$, seed coordinate $(r_0, c_0)$, similarity threshold $T_{sim}$.
- **Output:** Segmented binary region mask $S \in \{0, 255\}^{M \times N}$ (`uint8`).

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Read input grayscale image or synthesize distinct objects against dark background.
- **Step 2:** Select or automatically initialize seed point $(r_0, c_0)$ inside the target object.
- **Step 3:** Allocate segmented binary mask $S$ of size $M \times N$ initialized to 0, and visited boolean matrix $V$ initialized to False.
- **Step 4:** Initialize FIFO queue; enqueue $(r_0, c_0)$, mark $V(r_0, c_0) = \text{True}$, set $S(r_0, c_0) = 255$. Initialize running region sum and pixel count.
- **Step 5:** While queue is not empty: dequeue $(r, c)$. Compute reference intensity (either initial seed intensity $I(r_0, c_0)$ or dynamic running mean $\mu_{region}$).
- **Step 6:** For each 4-connected (or 8-connected) neighbor $(nr, nc)$: if within bounds and not visited, evaluate similarity condition: $|I(nr, nc) - \text{reference}| \le T_{sim}$.
- **Step 7:** If condition holds, mark $V(nr, nc) = \text{True}$, set $S(nr, nc) = 255$, update running mean, and enqueue $(nr, nc)$.
- **Step 8:** Render original image with marked seed and resulting segmented mask.

---

## 4. Structured Pseudocode
```text
ALGORITHM RegionGrowing(Image I, Point seed, float threshold):
    M, N = dimensions of I
    Initialize Segmented[M, N] as 0
    Initialize Visited[M, N] as False

    queue = [seed]
    Visited[seed.r, seed.c] = True
    Segmented[seed.r, seed.c] = 255
    seed_val = I[seed.r, seed.c]

    WHILE queue IS NOT EMPTY DO:
        curr = dequeue(queue)
        FOR EACH (nr, nc) IN Neighbors4(curr.r, curr.c) DO:
            IF 0 <= nr < M AND 0 <= nc < N THEN:
                IF NOT Visited[nr, nc] THEN:
                    Visited[nr, nc] = True
                    IF abs(int(I[nr, nc]) - int(seed_val)) <= threshold THEN:
                        Segmented[nr, nc] = 255
                        enqueue(queue, Point(nr, nc))
                    END IF
                END IF
            END IF
        END FOR
    END WHILE

    RETURN Segmented
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Homogeneity Criterion (Fixed Seed):** $H(R) = \text{True} \iff |I(x, y) - I(x_0, y_0)| \le T$
- **Dynamic Running Mean Criterion:** $H(R) = \text{True} \iff |I(x, y) - \mu_R| \le T \quad \text{where } \mu_R = \frac{1}{|R|} \sum_{(u, v) \in R} I(u, v)$
- **Connected Region Property:** Segmented set $R$ is a connected component where $\forall p, q \in R$, there exists a path within $R$.

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N)$ — in the worst case, every pixel is visited and evaluated at most 4 times (for 4-connectivity).
- **Space Complexity:** $O(M \times N)$ auxiliary storage for the queue and visited matrix.

---

## 7. Edge Cases & Boundary Handling
If threshold $T$ is too small, region terminates prematurely (under-segmentation); if $T$ is too large, region 'leaks' into the background (over-segmentation).

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Guaranteed spatial connectivity: Unlike global thresholding, region growing guarantees that the segmented object is 100% spatially connected without isolated stray pixels.
- Monotonic expansion: The segmented region set grows monotonically ($R_t \subseteq R_{t+1}$).
