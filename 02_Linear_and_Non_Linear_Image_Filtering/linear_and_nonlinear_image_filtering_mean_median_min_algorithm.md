# Algorithm Guide: Comprehensive Linear and Non-Linear Image Filtering Benchmark

## 1. Problem Statement & Objective
Perform unified side-by-side comparative evaluation of linear (Mean, Weighted Mean) and non-linear (Median, Min, Max) filters across Gaussian and Salt-and-Pepper noise regimes.

---

## 2. Input and Output Specifications
- **Input:** Grayscale image $I \in \mathbb{R}^{M \times N}$, contaminated independently with Gaussian and Salt-and-Pepper noise.
- **Output:** Filtered results for Mean, Weighted Mean, Median, Min, and Max filters (`uint8`).

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Load clean image; generate Gaussian noisy image $I_{gauss}$ and impulse noisy image $I_{sp}$.
- **Step 2:** Apply $3 \times 3$ Box Mean filter: $I_{mean}(i, j) = \frac{1}{9} \sum R$.
- **Step 3:** Apply $3 \times 3$ Gaussian Weighted Mean filter: $I_{weighted}(i, j) = \frac{1}{16} \sum (R \odot W)$.
- **Step 4:** Apply $3 \times 3$ Median filter: $I_{median}(i, j) = \text{median}(R)$.
- **Step 5:** Apply $3 \times 3$ Min filter: $I_{min}(i, j) = \min(R)$.
- **Step 6:** Apply $3 \times 3$ Max filter: $I_{max}(i, j) = \max(R)$.
- **Step 7:** Render complete comparative grid and analyze edge preservation vs noise suppression trade-offs.

---

## 4. Structured Pseudocode
```text
ALGORITHM ComprehensiveFilteringBenchmark(Image I):
    I_gauss = AddGaussianNoise(I)
    I_sp    = AddSaltAndPepperNoise(I)

    Filters = [BoxMean, WeightedMean, Median, Min, Max]
    
    FOR EACH noisy_img IN [I_gauss, I_sp] DO:
        FOR EACH f IN Filters DO:
            result = ApplyFilter(noisy_img, f, window_size=3)
            RecordVisualResult(result)
        END FOR
    END FOR

    DisplayGrid()
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Linear Superposition:** $f(a \cdot x_1 + b \cdot x_2) = a \cdot f(x_1) + b \cdot f(x_2)$ (Satisfied by Mean, violated by Median/Min/Max).
- **Rank-Order Definition:** For sorted window elements $x_{(1)} \le x_{(2)} \dots \le x_{(9)}$: $\text{Min} = x_{(1)}$, $\text{Median} = x_{(5)}$, $\text{Max} = x_{(9)}$.

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(F \cdot M \cdot N \cdot K^2)$ where $F$ is number of filter algorithms.
- **Space Complexity:** $O(F \cdot M \cdot N)$ memory to store comparative outputs.

---

## 7. Edge Cases & Boundary Handling
Mean filtering Salt-and-Pepper noise spreads the impulse into surrounding pixels, converting high-frequency noise into blotchy mid-gray artifacts.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Linearity divide: Mean filtering preserves average scene energy; Median/Min/Max filters are non-linear order-statistic transforms.
- Complementarity: Min filter suppresses salt noise (bright spikes); Max filter suppresses pepper noise (dark holes).
