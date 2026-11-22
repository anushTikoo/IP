# Viva & Theory Guide: Geometric Transformations (Resizing, Rotation, Flipping, Cropping)

## 1. First-Principles Analogy
> Geometric transformations are like manipulating a rubber sheet on which an image is printed: stretching or shrinking the sheet changes the size (resizing), spinning it around a central pin changes its orientation (rotation), turning the sheet over gives a mirror image (flipping), and taking a pair of shears to isolate a section is cropping.

---

## 2. What It Is (Concept & Definition)
- **Geometric Transformations**: Transformations that modify the spatial relationship between pixels rather than modifying the pixel values themselves.
- **Formal Definition**: A coordinate mapping $T$ such that:
  $$(x', y') = T(x, y)$$
- **Affine Transformation Properties**: Preserves collinearity (points lying on a straight line remain on a line) and ratios of distances between points along parallel lines.

---

## 3. Why We Do It (Motivation & Practical Use Cases)
- **Resizing (Spatial Rescaling)**: Standardizing image dimensions as inputs for deep neural networks (e.g., resizing high-res photos to $224 \times 224$ for ResNet / Vision Transformers).
- **Rotation**: Correcting skew in scanned documents (deskewing for OCR pipelines) or aerial drone survey alignment.
- **Flipping (Reflection)**: Data augmentation in computer vision (e.g., a car driving left is still a car when flipped to drive right).
- **Cropping**: Isolating a Region of Interest (ROI), such as face extraction from a surveillance frame before feeding to a facial recognition model.

---

## 4. How It Works (Algorithmic & Mathematical Breakdown)

### A. Affine Transformation Matrix
General 2D affine transformation in homogeneous coordinates:
$$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} a_{11} & a_{12} & t_x \\ a_{21} & a_{22} & t_y \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$

### B. Specific Transformation Formulations
1. **Horizontal Flipping (Mirror Reflection)**:
   $$x' = W - 1 - x, \quad y' = y$$
2. **Vertical Flipping**:
   $$x' = x, \quad y' = H - 1 - y$$
3. **Rotation by Angle $\theta$ about origin**:
   $$\begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$$
   For $90^\circ$ clockwise rotation: $\cos(90^\circ) = 0, \sin(90^\circ) = 1 \implies x' = y, y' = -x$.
4. **Resizing (Scaling)**:
   $$x' = s_x \cdot x, \quad y' = s_y \cdot y$$
   In inverse mapping, for each target pixel $(x', y')$: $x = x' / s_x, y = y' / s_y$.
5. **Cropping**: Sub-matrix coordinate window extraction:
   $$I_{cropped} = \{ I(y, x) \mid y_{min} \le y < y_{max}, x_{min} \le x < x_{max} \}$$

---

## 5. Code Walkthrough & Working

In [`image_geometric_transformations_resizing_rotation_flipping_cropping.py`](file:///home/anushtikoo/Downloads/IP/01_Basic_Image_Handling_and_Transformations/image_geometric_transformations_resizing_rotation_flipping_cropping.py):
- **Cell 1**: Imports required dependencies (`cv2`, `numpy`, `matplotlib.pyplot`).
- **Cell 2**: Synthetic image creation: draws colored shapes on a $256 \times 256$ canvas.
- **Cell 3**: Transformation implementations:
  - `img[:, ::-1]`: Step size `-1` on columns yields horizontal reflection with zero memory copy (strided array view).
  - `img[::-1, :]`: Step size `-1` on rows yields vertical reflection.
  - `cv2.resize(img, (128, 128))`: Downsamples image by $2\times$ along both axes.
  - `np.rot90(img, -1)`: Rotates 90 degrees clockwise by transposing and flipping.
  - `img[40:200, 40:200]`: Direct slicing creates a $160 \times 160$ cropped bounding box.
- **Cell 4**: Grid display showing all 5 outputs with clear titles.

---

## 6. High-Yield Viva Questions & Examiner Traps

### Q1: What is the time complexity of slicing `img[:, ::-1]` in NumPy?
**Answer**: It is $O(1)$ constant time! NumPy does not copy data when performing basic slicing or reversing; it simply alters the stride metadata of the `ndarray` (negative horizontal stride). The memory is only touched during rendering or copy.

### Q2: What causes aliasing during image downsampling, and how can it be prevented?
**Answer**: According to the Nyquist-Shannon sampling theorem, sampling must occur at greater than twice the highest spatial frequency ($f_s > 2f_{max}$). When downsampling, high spatial frequency details exceed the new Nyquist limit and fold into lower frequencies, creating Moiré patterns and jagged edges. To prevent this, apply an anti-aliasing low-pass (Gaussian) filter **before** downsampling.

### Q3: When rotating an image by an arbitrary angle like $45^\circ$, why do black triangular corners appear?
**Answer**: A rectangle rotated by an angle other than multiples of $180^\circ$ requires a larger enclosing bounding box to prevent clipping:
$$W_{new} = W |\cos \theta| + H |\sin \theta|, \quad H_{new} = W |\sin \theta| + H |\cos \theta|$$
Any target pixels outside the original rotated rectangle fall outside the source image boundary and default to zero (black).
