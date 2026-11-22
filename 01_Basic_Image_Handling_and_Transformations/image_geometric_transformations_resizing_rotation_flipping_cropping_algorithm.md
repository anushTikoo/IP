# Algorithm Guide: Geometric Image Transformations: Resizing, Rotation, Flipping, and Cropping

## 1. Problem Statement & Objective
Apply spatial coordinate mapping using nearest-neighbor interpolation, inverse rotation around the center, and 2D slicing for cropping and reflections.

---

## 2. Input and Output Specifications
- **Input:** Image matrix $I$ of shape $M \times N$, target scaling factors $(s_x, s_y)$, rotation angle $\theta$, and bounding box $(y_{min}, y_{max}, x_{min}, x_{max})$.
- **Output:** Transformed matrices: Resized $I_{resized}$, Rotated $I_{rotated}$, Cropped $I_{cropped}$, Flipped $I_{hflip}, I_{vflip}$.

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Compute output dimensions for resizing: $M_{new} = \text{round}(M \cdot s_y)$, $N_{new} = \text{round}(N \cdot s_x)$.
- **Step 2 [Nearest Neighbor Resizing]:** For each output coordinate $(y', x')$, calculate source coordinate $(y, x) = (\text{round}(y' / s_y), \text{round}(x' / s_x))$. Clamp to boundaries and assign $I_{resized}(y', x') = I(y, x)$.
- **Step 3 [Rotation via Backward Mapping]:** Determine center $(y_c, x_c) = (M/2, N/2)$. Convert $\theta$ to radians.
- **Step 4:** For each output pixel $(y', x')$, compute centered offsets $(\Delta y', \Delta x') = (y' - y_c, x' - x_c)$ and backward rotate: $x = \text{round}(x_c + \Delta x' \cos\theta + \Delta y' \sin\theta)$, $y = \text{round}(y_c - \Delta x' \sin\theta + \Delta y' \cos\theta)$. If inside source bounds, assign value; else assign 0.
- **Step 5 [Cropping]:** Slice rectangular region: $I_{cropped} = I[y_{min}:y_{max}, x_{min}:x_{max}]$.
- **Step 6 [Flipping]:** Invert row/column indexing: $I_{hflip} = I[:, ::-1]$, $I_{vflip} = I[::-1, :]$.
- **Step 7:** Plot all transformed images.

---

## 4. Structured Pseudocode
```text
ALGORITHM GeometricTransformations(Image I, float sx, float sy, float theta, Rect crop):
    M, N = dimensions of I
    M_new = round(M * sy)
    N_new = round(N * sx)
    Initialize Resized[M_new, N_new], Rotated[M, N] as uint8

    // 1. Resizing (Nearest Neighbor)
    FOR y_prime = 0 TO M_new - 1 DO:
        FOR x_prime = 0 TO N_new - 1 DO:
            y = min(M - 1, max(0, round(y_prime / sy)))
            x = min(N - 1, max(0, round(x_prime / sx)))
            Resized[y_prime, x_prime] = I[y, x]
        END FOR
    END FOR

    // 2. Backward Rotation around Image Center
    yc = M / 2, xc = N / 2
    rad = radians(theta)
    FOR y_prime = 0 TO M - 1 DO:
        FOR x_prime = 0 TO N - 1 DO:
            dy = y_prime - yc
            dx = x_prime - xc
            orig_x = round(xc + dx * cos(rad) + dy * sin(rad))
            orig_y = round(yc - dx * sin(rad) + dy * cos(rad))
            IF 0 <= orig_x < N AND 0 <= orig_y < M THEN:
                Rotated[y_prime, x_prime] = I[orig_y, orig_x]
            ELSE:
                Rotated[y_prime, x_prime] = 0
            END IF
        END FOR
    END FOR

    Cropped = I[crop.ymin : crop.ymax, crop.xmin : crop.xmax]
    HFlip = I[:, ::-1]
    VFlip = I[::-1, :]

    RETURN Resized, Rotated, Cropped, HFlip, VFlip
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Backward Rotation Matrix:** $\begin{bmatrix} x - x_c \\ y - y_c \end{bmatrix} = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix} \begin{bmatrix} x' - x_c \\ y' - y_c \end{bmatrix}$
- **Nearest Neighbor Scaling:** $(x, y) = (\text{round}(x' / s_x), \text{round}(y' / s_y))$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M_{new} \times N_{new} + M \times N)$ dominated by backward coordinate calculation.
- **Space Complexity:** $O(M_{new} \times N_{new} + M \times N)$ auxiliary storage for transformed grids.

---

## 7. Edge Cases & Boundary Handling
Discretization in forward mapping causes 'holes' / gaps in output; backward mapping (inverse mapping) guarantees every target pixel is filled.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Completeness: Every pixel in output raster is explicitly assigned a source or background intensity.
- Center preservation: The rotational pivot point $(y_c, x_c)$ remains stationary under rotation.
