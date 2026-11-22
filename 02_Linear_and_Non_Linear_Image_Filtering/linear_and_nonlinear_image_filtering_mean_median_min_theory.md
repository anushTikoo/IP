# Viva & Theory Guide: Linear vs Non-Linear Image Filtering (Mean, Median, Min Comparison)

## 1. First-Principles Analogy
> Filtering is like applying three different voting rules to noisy data:
> 1. **Mean (Linear)**: Everyone's opinion is averaged. Great for general consensus, but a single extremist pulls the whole average off-course.
> 2. **Median (Non-Linear)**: The group lines up and the exact middle person decides. Extremists at either end have zero influence.
> 3. **Min (Non-Linear)**: The most pessimistic person in the group wins every single debate, dragging everyone down into darkness.

---

## 2. What It Is (Concept & Definition)
- **Linear Filtering**: An operation where the output is a linear combination of input pixels ($g = \sum w_i p_i$). Obey the superposition principle. Examples: Mean, Weighted Mean, Gaussian filters.
- **Non-Linear Filtering**: An operation that cannot be formulated as a linear matrix convolution because the relationship involves conditional, rank-order, or sorting logic. Examples: Median, Min, Max, Bilateral filters.
- **Comparative Taxonomy**:
  | Filter | Class | Primary Target Noise | Edge Preservation | Brightness Effect |
  | :--- | :--- | :--- | :--- | :--- |
  | **Mean** | Linear | Gaussian / Thermal | Poor (Blurs edges) | Neutral (Preserves mean) |
  | **Weighted Mean** | Linear | Gaussian / Thermal | Moderate (Preserves center) | Neutral (Preserves mean) |
  | **Median** | Non-Linear | Salt & Pepper / Impulse | Excellent (Preserves steps) | Neutral (Preserves median) |
  | **Min** | Non-Linear | Salt (Bright spikes) | Poor (Expands dark edges) | Darkens overall image |

---

## 3. Why We Do It (Motivation & Practical Use Cases)
- Real-world imaging pipelines encounter distinct noise models depending on the physical sensor physics:
  - *Thermal agitation of electrons* in CMOS sensors produces **additive Gaussian noise** $\implies$ Mean / Gaussian filter.
  - *Bit transmission errors or stuck dead/hot pixels* create **impulse salt-and-pepper noise** $\implies$ Median filter.
  - *Specular reflections and bright flash artifacts* create **salt noise** $\implies$ Min filter.
- Understanding which filter to choose is the most critical decision in image pre-processing.

---

## 4. How It Works (Algorithmic & Mathematical Breakdown)

For a local neighborhood $S_{xy}$ of size $3 \times 3$:
1. **Mean Output**:

   $$
   g_{mean}(x, y) = \frac{1}{9} \sum_{(s, t) \in S_{xy}} f(x+s, y+t)
   $$
2. **Median Output**:

   $$
   g_{median}(x, y) = \text{Median}_{(s, t) \in S_{xy}} \{ f(x+s, y+t) \}
   $$
3. **Min Output**:

   $$
   g_{min}(x, y) = \min_{(s, t) \in S_{xy}} \{ f(x+s, y+t) \}
   $$

---

## 5. Code Walkthrough & Working

In [`linear_and_nonlinear_image_filtering_mean_median_min.py`](file:///home/anushtikoo/Downloads/IP/02_Linear_and_Non_Linear_Image_Filtering/linear_and_nonlinear_image_filtering_mean_median_min.py):
- **Cell 1**: Imports `numpy` and `matplotlib.pyplot`.
- **Cell 2**: Generates a noisy test pattern combining gray backgrounds and random pixel perturbations.
- **Cell 3**: Runs all three filters simultaneously inside a unified spatial convolution pass:
  - Iterates across interior rows and columns.
  - Extracts the $3 \times 3$ sub-matrix `region`.
  - Computes `mean_out[i, j] = int(np.sum(region) // 9)`.
  - Computes `median_out[i, j] = int(np.median(region))`.
  - Computes `min_out[i, j] = np.min(region)`.
- **Cell 4**: 4-panel subplot comparing Original Noisy, Mean Filter, Median Filter, and Min Filter side by side.

---

## 6. High-Yield Viva Questions & Examiner Traps

### Q1: What is the mathematical definition of a linear system, and prove why a mean filter is linear?
**Answer**: A system $\mathcal{H}$ is linear if:
$$
\mathcal{H}\{a f_1(x, y) + b f_2(x, y)\} = a \mathcal{H}\{f_1(x, y)\} + b \mathcal{H}\{f_2(x, y)\}
$$
For a mean filter:
$$
\mathcal{H}\{a f_1 + b f_2\} = \frac{1}{N}\sum (a f_1 + b f_2) = a\left(\frac{1}{N}\sum f_1\right) + b\left(\frac{1}{N}\sum f_2\right) = a \mathcal{H}\{f_1\} + b \mathcal{H}\{f_2\}
$$
Since both scalability and additivity hold, the mean filter is strictly linear.

### Q2: Why does a mean filter fail on impulse noise while median succeeds?
**Answer**: Impulse noise pixels are mathematical outliers with extreme values ($0$ or $255$). In a linear sum, an outlier contributes its full numeric magnitude, altering the arithmetic mean substantially:
$$
\text{Mean} = \frac{8 \times 50 + 255}{9} = \frac{655}{9} \approx 72.8
$$
(a $45.6\%$ error).
In contrast, median is rank-order based; the outlier is moved to the far end of the sorted sequence and has zero mathematical influence on the central rank value.

### Q3: What is the computational disadvantage of a median filter compared to a mean filter?
**Answer**: A mean filter requires only additions and a single scalar division, which can be implemented in $O(1)$ time per pixel using **Integral Images (Summed Area Tables)**. A median filter requires finding the median rank, which requires sorting or maintaining a running histogram, making it significantly more computationally intensive ($O(k)$ to $O(k^2)$).
