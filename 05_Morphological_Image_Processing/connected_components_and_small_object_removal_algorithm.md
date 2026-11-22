# Algorithm Guide: Connected Components Labeling and Small Object Removal

## 1. Problem Statement & Objective
Identify and uniquely label disconnected binary foreground objects using connected-component analysis and eliminate noise specks below a prescribed area threshold.

---

## 2. Input and Output Specifications
- **Input:** Binary image $I \in \{0, 1\}^{M \times N}$, connectivity type (4 or 8), minimum area threshold $T_{area}$.
- **Output:** Integer label map $L \in \mathbb{Z}^{M \times N}$, component count $K$, filtered binary image $I_{filtered}$.

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Read input binary image containing primary objects and scattered small noise artifacts.
- **Step 2:** Allocate label matrix $L$ initialized to 0 and visited boolean matrix $V$ initialized to False.
- **Step 3 [Connected Components via BFS/Queue]:** Initialize `current_label = 0`.
- **Step 4:** Scan raster $(i, j)$: If $I(i, j) == 1$ and not $V(i, j)$, increment `current_label` by 1. Enqueue $(i, j)$ and mark visited.
- **Step 5:** While queue is not empty: dequeue $(r, c)$, assign $L(r, c) = current\_label$, and examine its 8-connected neighbors. If neighbor has value 1 and is unvisited, mark visited and enqueue.
- **Step 6 [Area Filtering]:** For each label $k \in [1, current\_label]$, count total pixels $A_k = \sum [L == k]$.
- **Step 7:** If $A_k < T_{area}$, set all pixels with label $k$ to 0 in output image $I_{filtered}$; otherwise set to 255.
- **Step 8:** Display colored label map and cleaned binary image.

---

## 4. Structured Pseudocode
```text
ALGORITHM ConnectedComponentsFilter(BinaryImage I, int min_area):
    M, N = dimensions of I
    Initialize Label[M, N] as 0
    Initialize Visited[M, N] as False
    current_label = 0

    FOR i = 0 TO M - 1 DO:
        FOR j = 0 TO N - 1 DO:
            IF I[i, j] == 1 AND NOT Visited[i, j] THEN:
                current_label = current_label + 1
                queue = [(i, j)]
                Visited[i, j] = True
                
                WHILE queue IS NOT EMPTY DO:
                    r, c = dequeue(queue)
                    Label[r, c] = current_label
                    FOR EACH (nr, nc) IN Neighbors8(r, c) DO:
                        IF 0 <= nr < M AND 0 <= nc < N THEN:
                            IF I[nr, nc] == 1 AND NOT Visited[nr, nc] THEN:
                                Visited[nr, nc] = True
                                enqueue(queue, (nr, nc))
                            END IF
                        END IF
                    END FOR
                END WHILE
            END IF
        END FOR
    END FOR

    // Area Filtering
    Initialize Cleaned[M, N] as 0
    FOR k = 1 TO current_label DO:
        area_k = count(Label == k)
        IF area_k >= min_area THEN:
            Cleaned[Label == k] = 255
        END IF
    END FOR

    RETURN Label, Cleaned, current_label
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Component Equivalence:** Pixels $p, q$ share label $k$ iff there exists a path $(p = z_0, z_1, \dots, z_n = q)$ where every $z_i \in \text{Foreground}$.
- **Component Area:** $Area(k) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} \mathbb{I}(Label(x, y) == k)$
- **Threshold Filter:** $I_{clean}(x, y) = 1 \iff Label(x, y) = k \text{ and } Area(k) \ge T_{area}$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N)$ — each pixel is enqueued and dequeued at most once.
- **Space Complexity:** $O(M \times N)$ memory for queue, visited table, and label matrix.

---

## 7. Edge Cases & Boundary Handling
Objects touching boundary must not trigger index out-of-bounds in neighbor exploration; neighbor coordinates must be clamped to $[0, M-1] 	imes [0, N-1]$.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Uniqueness: Every connected component receives a strictly unique integer ID.
- Monotonic area rejection: No object with area $< T_{area}$ survives in $I_{filtered}$.
