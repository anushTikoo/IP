# Digital Image Processing Lab Experiments

This repository contains Python (`.py`) and Jupyter Notebook (`.ipynb`) implementations of all Image Processing lab experiments.

## Repository Structure

```
IP/
├── 01_Basic_Image_Handling_and_Transformations/
│   ├── basic_image_manipulation_and_transformations.py / .ipynb
│   ├── grayscale_conversion_and_color_inversion.py / .ipynb
│   ├── image_geometric_transformations_resizing_rotation_flipping_cropping.py / .ipynb
│   └── images/
├── 02_Linear_and_Non_Linear_Image_Filtering/
│   ├── linear_and_nonlinear_image_filtering_mean_median_min.py / .ipynb
│   ├── filtering_with_mean_and_weighted_mean_filter.py / .ipynb
│   ├── filtering_with_median_filter.py / .ipynb
│   └── filtering_with_min_filter.py / .ipynb
├── 03_Histogram_Processing_and_Equalization/
│   ├── histogram_processing_contrast_stretching_equalization_matching.py / .ipynb
│   ├── contrast_stretching.py / .ipynb
│   ├── histogram_equalization.py / .ipynb
│   └── histogram_matching_specification.py / .ipynb
├── 04_Edge_Detection_Prewitt_Sobel_Laplacian/
│   ├── edge_detection_prewitt_sobel_laplacian_comparison.py / .ipynb
│   ├── prewitt_edge_detection.py / .ipynb
│   ├── sobel_edge_detection.py / .ipynb
│   └── laplacian_edge_detection.py / .ipynb
├── 05_Morphological_Image_Processing/
│   ├── morphological_operations_complete.py / .ipynb
│   ├── morphological_erosion_and_dilation.py / .ipynb
│   ├── morphological_opening_and_closing.py / .ipynb
│   ├── connected_components_and_small_object_removal.py / .ipynb
│   ├── morphological_boundary_extraction.py / .ipynb
│   └── zhang_suen_skeletonization.py / .ipynb
├── 06_Image_Segmentation_Edge_and_Region_Based/
│   ├── image_segmentation_edge_and_region_based.py / .ipynb
│   ├── edge_based_segmentation_sobel.py / .ipynb
│   └── region_based_segmentation_region_growing.py / .ipynb
├── 07_Lossless_Image_Compression_Huffman_RLE_LZW/
│   ├── lossless_image_compression_huffman_rle_lzw.py / .ipynb
│   ├── huffman_coding_image_compression.py / .ipynb
│   ├── run_length_encoding_rle_image_compression.py / .ipynb
│   └── lzw_symbol_based_image_compression.py / .ipynb
├── 08_Object_Detection_and_Contour_Analysis/
│   ├── object_detection_and_contour_analysis.py / .ipynb
│   ├── contour_detection_and_bounding_box_extraction.py / .ipynb
│   └── shape_feature_extraction_area_centroid_circularity.py / .ipynb
├── requirements.txt
└── README.md
```

## Formatting & Memorization Optimization
- **Python Files (`.py`)**: Individual cell blocks are separated by `# ----`. Code is streamlined and optimized for quick exam and interview memorization (~39 lines per file on average) while strictly preserving manual first-principles algorithms (no cheating with high-level library shortcuts).
- **Notebook Files (`.ipynb`)**: Standard Jupyter Notebook format containing individual runnable code cells corresponding to each cell block.

## Requirements & Setup
Install required dependencies using:
```bash
pip install -r requirements.txt
```
