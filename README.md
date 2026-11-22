# Digital Image Processing Lab Experiments & Viva Preparation Guide

This repository contains complete implementations, comprehensive theory guides, and formal academic step-by-step algorithms for all Digital Image Processing (DIP) lab experiments. Every experiment includes concise Python scripts (`.py`), interactive Jupyter Notebooks (`.ipynb`), an exhaustive **Viva & Theory Guide (`_theory.md`)**, and a formal **Step-by-Step Algorithm Guide (`_algorithm.md`)**.

## Repository Structure

```
IP/
├── 01_Basic_Image_Handling_and_Transformations/
│   ├── basic_image_manipulation_and_transformations.py / .ipynb / _theory.md / _algorithm.md
│   ├── grayscale_conversion_and_color_inversion.py / .ipynb / _theory.md / _algorithm.md
│   ├── image_geometric_transformations_resizing_rotation_flipping_cropping.py / .ipynb / _theory.md / _algorithm.md
│   └── images/
├── 02_Linear_and_Non_Linear_Image_Filtering/
│   ├── linear_and_nonlinear_image_filtering_mean_median_min.py / .ipynb / _theory.md / _algorithm.md
│   ├── filtering_with_mean_and_weighted_mean_filter.py / .ipynb / _theory.md / _algorithm.md
│   ├── filtering_with_median_filter.py / .ipynb / _theory.md / _algorithm.md
│   └── filtering_with_min_filter.py / .ipynb / _theory.md / _algorithm.md
├── 03_Histogram_Processing_and_Equalization/
│   ├── histogram_processing_contrast_stretching_equalization_matching.py / .ipynb / _theory.md / _algorithm.md
│   ├── contrast_stretching.py / .ipynb / _theory.md / _algorithm.md
│   ├── histogram_equalization.py / .ipynb / _theory.md / _algorithm.md
│   └── histogram_matching_specification.py / .ipynb / _theory.md / _algorithm.md
├── 04_Edge_Detection_Prewitt_Sobel_Laplacian/
│   ├── edge_detection_prewitt_sobel_laplacian_comparison.py / .ipynb / _theory.md / _algorithm.md
│   ├── prewitt_edge_detection.py / .ipynb / _theory.md / _algorithm.md
│   ├── sobel_edge_detection.py / .ipynb / _theory.md / _algorithm.md
│   └── laplacian_edge_detection.py / .ipynb / _theory.md / _algorithm.md
├── 05_Morphological_Image_Processing/
│   ├── morphological_operations_complete.py / .ipynb / _theory.md / _algorithm.md
│   ├── morphological_erosion_and_dilation.py / .ipynb / _theory.md / _algorithm.md
│   ├── morphological_opening_and_closing.py / .ipynb / _theory.md / _algorithm.md
│   ├── connected_components_and_small_object_removal.py / .ipynb / _theory.md / _algorithm.md
│   ├── morphological_boundary_extraction.py / .ipynb / _theory.md / _algorithm.md
│   └── zhang_suen_skeletonization.py / .ipynb / _theory.md / _algorithm.md
├── 06_Image_Segmentation_Edge_and_Region_Based/
│   ├── image_segmentation_edge_and_region_based.py / .ipynb / _theory.md / _algorithm.md
│   ├── edge_based_segmentation_sobel.py / .ipynb / _theory.md / _algorithm.md
│   └── region_based_segmentation_region_growing.py / .ipynb / _theory.md / _algorithm.md
├── 07_Lossless_Image_Compression_Huffman_RLE_LZW/
│   ├── lossless_image_compression_huffman_rle_lzw.py / .ipynb / _theory.md / _algorithm.md
│   ├── huffman_coding_image_compression.py / .ipynb / _theory.md / _algorithm.md
│   ├── run_length_encoding_rle_image_compression.py / .ipynb / _theory.md / _algorithm.md
│   └── lzw_symbol_based_image_compression.py / .ipynb / _theory.md / _algorithm.md
├── 08_Object_Detection_and_Contour_Analysis/
│   ├── object_detection_and_contour_analysis.py / .ipynb / _theory.md / _algorithm.md
│   ├── contour_detection_and_bounding_box_extraction.py / .ipynb / _theory.md / _algorithm.md
│   └── shape_feature_extraction_area_centroid_circularity.py / .ipynb / _theory.md / _algorithm.md
├── requirements.txt
├── setup_jupyter.md
└── README.md
```

## Features per Topic

1. **Python Files (`.py`)**:
   - Streamlined for rapid exam and viva memorization (~39 lines per file on average).
   - Cell blocks separated by `# ----`.
   - Strictly preserves manual first-principles algorithms (manual convolution loops, CDF calculations, Huffman binary tree generation, LZW dynamic dictionaries, RLE loops, Zhang-Suen iterations, Region Growing queues).
   - Fully standalone with synthetic fallback data.

2. **Jupyter Notebooks (`.ipynb`)**:
   - 1:1 cell parity with `.py` scripts for interactive execution and visualization.

3. **Viva & Theory Guides (`_theory.md`)**:
   - **First-Principles Analogy**: A vivid everyday metaphor at the very top for instant intuitive recall.
   - **What It Is (Concept & Definition)**: Formal definitions, domain classification, and mathematical representations.
   - **Why We Do It (Motivation & Practical Use Cases)**: Real-world applications, engineering trade-offs, and failure cases.
   - **How It Works (Algorithmic & Mathematical Breakdown)**: Mathematical derivations, kernel matrices, time/space complexities, and boundary conditions.
   - **Code Walkthrough & Working**: Cell-by-cell architectural breakdown linking directly to the Python code.
   - **High-Yield Viva Questions & Examiner Traps**: 3 to 5 realistic oral exam questions with model technical answers.

4. **Step-by-Step Algorithm Guides (`_algorithm.md`)**:
   - **Problem Statement & Objective**: Clear specification of the task.
   - **Input and Output Specifications**: Explicit data types, tensor shapes, dynamic ranges, and parameters.
   - **Step-by-Step Formal Algorithm**: Classical academic lab-record / exam format (`Step 1`, `Step 2`, ...).
   - **Structured Pseudocode**: Clean, language-agnostic procedural pseudocode.
   - **Mathematical Formulations & Transformation Equations**: Exact mathematical formulas and kernel matrices.
   - **Computational Complexity & Memory Footprint**: Formal Big-O analysis ($O(M \times N)$ time and auxiliary space).
   - **Edge Cases & Boundary Handling**: Border padding, overflow clipping, and division-by-zero prevention.
   - **Viva Quick-Check**: Core algorithmic invariants and exam check-points.

## Requirements & Setup
Install required dependencies using:
```bash
pip install -r requirements.txt
```
