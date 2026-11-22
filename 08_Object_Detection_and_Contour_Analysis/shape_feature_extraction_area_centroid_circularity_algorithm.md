# Algorithm Guide: Shape Feature Extraction: Area, Centroid, and Circularity

## 1. Problem Statement & Objective
Compute mathematical geometric shape descriptors (Area via Green's theorem, spatial moments for Centroid, Perimeter, and Circularity / Compactness) for object recognition and classification.

---

## 2. Input and Output Specifications
- **Input:** Contour coordinate set $C = \{(x_0, y_0), (x_1, y_1), \dots, (x_{n-1}, y_{n-1})\}$ representing a closed boundary.
- **Output:** Geometric descriptors: Area $A$, Perimeter $P$, Centroid $(\bar{x}, \bar{y})$, Circularity $C_{circ}$, and Aspect Ratio $AR$.

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Extract closed contour polygon $C$ for target object.
- **Step 2 [Area Calculation via Green's Theorem / Surveyor's Formula]:** Compute $A = \frac{1}{2} \left| \sum_{i=0}^{n-1} (x_i y_{i+1} - x_{i+1} y_i) \right|$ with wrap-around $(x_n, y_n) = (x_0, y_0)$.
- **Step 3 [Perimeter Calculation]:** Compute sum of Euclidean distances between adjacent boundary vertices: $P = \sum_{i=0}^{n-1} \sqrt{(x_{i+1} - x_i)^2 + (y_{i+1} - y_i)^2}$.
- **Step 4 [Spatial Moments for Centroid]:** Compute spatial moments $m_{00} = A$, $m_{10} = \sum_{(x,y) \in R} x$, $m_{01} = \sum_{(x,y) \in R} y$. Determine centroid coordinates: $\bar{x} = m_{10} / m_{00}$, $\bar{y} = m_{01} / m_{00}$.
- **Step 5 [Circularity / Compactness Metric]:** Calculate compactness ratio: $C_{circ} = \frac{4\pi A}{P^2}$. (Ideal circle $= 1.0$, square $\approx 0.785$, elongated/complex shapes $\to 0$).
- **Step 6:** Classify shape based on circularity thresholds (e.g. $C_{circ} > 0.85 \implies \text{Circle}$, $0.70 < C_{circ} \le 0.85 \implies \text{Square/Polygon}$, $C_{circ} \le 0.70 \implies \text{Elongated/Irregular}$).
- **Step 7:** Render object with plotted centroid marker and annotated feature values.

---

## 4. Structured Pseudocode
```text
ALGORITHM ShapeFeatureExtraction(Contour C):
    n = length(C)
    
    // 1. Area via Green's Theorem
    area_sum = 0
    FOR i = 0 TO n - 1 DO:
        curr = C[i]
        nxt  = C[(i + 1) % n]
        area_sum = area_sum + (curr.x * nxt.y - nxt.x * curr.y)
    END FOR
    Area = abs(area_sum) / 2.0

    // 2. Perimeter via Arc Length
    Perimeter = 0.0
    FOR i = 0 TO n - 1 DO:
        curr = C[i]
        nxt  = C[(i + 1) % n]
        Perimeter = Perimeter + sqrt((nxt.x - curr.x)^2 + (nxt.y - curr.y)^2)
    END FOR

    // 3. Centroid via Moments
    M = ComputeSpatialMoments(C)
    cx = M.m10 / M.m00
    cy = M.m01 / M.m00

    // 4. Circularity
    Circularity = (4.0 * pi * Area) / (Perimeter^2)

    RETURN Area, Perimeter, Point(cx, cy), Circularity
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Green's Theorem for Polygon Area:** $A = \frac{1}{2} \left| \sum_{i=0}^{n-1} (x_i y_{i+1} - x_{i+1} y_i) \right|$
- **Euclidean Perimeter:** $P = \sum_{i=0}^{n-1} \sqrt{(x_{i+1} - x_i)^2 + (y_{i+1} - y_i)^2}$
- **Centroid Coordinates:** $\bar{x} = \frac{m_{10}}{m_{00}}, \quad \bar{y} = \frac{m_{01}}{m_{00}} \quad \text{where } m_{pq} = \iint x^p y^q dx dy$
- **Circularity (Isoperimetric Quotient):** $C = \frac{4\pi A}{P^2} \le 1.0$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(n)$ where $n$ is the number of vertices in contour polygon.
- **Space Complexity:** $O(1)$ constant auxiliary storage for feature scalars.

---

## 7. Edge Cases & Boundary Handling
Contour with fewer than 3 vertices cannot enclose 2D area ($A=0$); check $n \ge 3$ before calculating circularity to avoid division by zero.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Scale & Rotation Invariance: Circularity $C = 4\pi A / P^2$ is strictly dimensionless, remaining invariant under uniform scaling and rigid 2D rotation.
- Isoperimetric Inequality: For any planar shape, $P^2 \ge 4\pi A$, with equality holding strictly if and only if the shape is a circle ($C=1.0$).
