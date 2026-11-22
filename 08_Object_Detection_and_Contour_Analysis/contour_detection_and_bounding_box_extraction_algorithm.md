# Algorithm Guide: Contour Detection and Bounding Box Extraction

## 1. Problem Statement & Objective
Detect external object boundaries using topological contour tracing, extract axis-aligned bounding boxes (AABB), and compute spatial bounding envelopes.

---

## 2. Input and Output Specifications
- **Input:** Binary or segmented image $I \in \{0, 255\}^{M \times N}$.
- **Output:** Contour coordinate lists $\{C_k\}$, Bounding boxes $[(x_{min}, y_{min}, w, h)_k]$, and visualization overlays.

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Read input image; binarize using Otsu's thresholding if input is grayscale.
- **Step 2:** Trace external boundaries of connected components using 8-connected border following (Suzuki algorithm or Moore-Neighbor tracing).
- **Step 3:** For each detected contour $C_k = [(x_1, y_1), (x_2, y_2), \dots, (x_p, y_p)]$:
- **Step 4:** Find coordinate extrema: $x_{min} = \min(x_i)$, $x_{max} = \max(x_i)$, $y_{min} = \min(y_i)$, $y_{max} = \max(y_i)$.
- **Step 5:** Compute bounding box width $w = x_{max} - x_{min} + 1$ and height $h = y_{max} - y_{min} + 1$.
- **Step 6:** Draw green boundary polygons along contour points.
- **Step 7:** Draw red rectangular bounding boxes $[x_{min}, y_{min}, w, h]$ over detected objects.
- **Step 8:** Display annotated image with bounding box metrics.

---

## 4. Structured Pseudocode
```text
ALGORITHM ContourAndBoundingBox(BinaryImage B):
    contours = TraceContours(B, mode=EXTERNAL, method=CHAIN_APPROX_SIMPLE)
    boxes = []

    FOR EACH c IN contours DO:
        x_coords = [pt.x FOR pt IN c]
        y_coords = [pt.y FOR pt IN c]
        
        xmin, xmax = min(x_coords), max(x_coords)
        ymin, ymax = min(y_coords), max(y_coords)
        
        w = xmax - xmin + 1
        h = ymax - ymin + 1
        boxes.append((xmin, ymin, w, h))
    END FOR

    Annotated = DrawContoursAndBoxes(B, contours, boxes)
    RETURN contours, boxes, Annotated
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Axis-Aligned Bounding Box (AABB):** $\mathcal{B}(C) = [x_{min}, y_{min}, x_{max} - x_{min}, y_{max} - y_{min}]$
- **Aspect Ratio:** $AR = \frac{w}{h} = \frac{x_{max} - x_{min} + 1}{y_{max} - y_{min} + 1}$
- **Extent:** $Extent = \frac{\text{Contour Area}}{w \times h}$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N)$ for border following and bounding box extraction.
- **Space Complexity:** $O(P)$ where $P$ is total perimeter vertices in all contours.

---

## 7. Edge Cases & Boundary Handling
Objects touching image border may have open contours unless outer 1-pixel border of image is zero-padded prior to tracing.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Bounding box containment: Every contour vertex $(x_i, y_i) \in C_k$ satisfies $x_{min} \le x_i \le x_{min} + w$ and $y_{min} \le y_i \le y_{min} + h$.
- Topological completeness: Each closed contour separates an interior foreground region from background.
