# Algorithm Guide: Comprehensive Lossless Image Compression Benchmark

## 1. Problem Statement & Objective
Side-by-side benchmark of Huffman, RLE, and LZW compression algorithms across varied image textures (binary masks, smooth gradients, and textured imagery).

---

## 2. Input and Output Specifications
- **Input:** Multiple image test cases: synthetic binary mask, clean gradient, and photographic grayscale image.
- **Output:** Comparative table containing Compressed Size, Compression Ratio ($CR$), Encoding Time, and Decoding Time for each algorithm.

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Prepare test images with varying spatial entropy (Binary Mask, Low-Entropy Graphic, Natural Photo).
- **Step 2:** Run Huffman Coding on each test image; record compressed bits, runtime, and verify $MSE = 0$.
- **Step 3:** Run RLE Coding on each test image; record total tuples and compression ratio.
- **Step 4:** Run LZW Coding on each test image; record dictionary size and compressed code count.
- **Step 5:** Tabulate metrics into a structured comparative DataFrame.
- **Step 6:** Display visual comparison and compression performance trade-off charts.

---

## 4. Structured Pseudocode
```text
ALGORITHM CompressionBenchmark(Images test_suite):
    Algorithms = [HuffmanCoding, RunLengthEncoding, LZWCompression]

    FOR EACH img IN test_suite DO:
        FOR EACH algo IN Algorithms DO:
            compressed, reconstructed, time_taken = algo(img)
            cr = OriginalSize(img) / CompressedSize(compressed)
            ASSERT (reconstructed == img)  // Lossless check
            LogMetric(img.name, algo.name, cr, time_taken)
        END FOR
    END FOR

    DisplayMetricsTable()
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Compression Ratio ($CR$):** $CR = \frac{\text{Uncompressed Bytes}}{\text{Compressed Bytes}}$
- **Space Savings ($SS$):** $SS = \left(1 - \frac{1}{CR}\right) \times 100\%$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(N)$ linear time across all three algorithms for raster data.
- **Space Complexity:** $O(N)$ auxiliary buffers for encoded representation.

---

## 7. Edge Cases & Boundary Handling
RLE excels on binary mask with large solid patches ($CR > 20$), but exhibits expansion on natural photo; Huffman consistently compresses natural photo near entropy ($CR pprox 1.2 - 1.5$).

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- Strict losslessness: All three algorithms achieve $MSE = 0$ and $PSNR = \infty$.
- Shannon limit: No algorithm compresses below Shannon entropy without information loss.
