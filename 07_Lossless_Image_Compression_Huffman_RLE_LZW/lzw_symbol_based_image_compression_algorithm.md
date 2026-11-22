# Algorithm Guide: Lempel-Ziv-Welch (LZW) Dictionary-Based Image Compression

## 1. Problem Statement & Objective
Compress image pixel streams without prior statistical knowledge by dynamically constructing an adaptive phrase dictionary on-the-fly during encoding.

---

## 2. Input and Output Specifications
- **Input:** Flattened pixel sequence $P$ of image $I \in \mathbb{R}^{M \times N}$.
- **Output:** Compressed code list $C$, dynamically formed dictionary, decompressed image $I_{rec}$, and compression ratio $CR$.

---

## 3. Step-by-Step Formal Algorithm
- **Step 1:** Initialize dictionary mapping all 256 individual byte values $(0 \dots 255)$ to integer codes $0 \dots 255$. Next available code index $= 256$.
- **Step 2:** Initialize string accumulator $P = \text{empty}$.
- **Step 3 [Encoding Loop]:** For each symbol $C$ in input byte sequence:
- **Step 4:** If phrase $P + C$ exists in dictionary, update $P = P + C$.
- **Step 5:** Else, output dictionary code for $P$; insert new phrase $P + C$ into dictionary with next available code index; reset $P = C$.
- **Step 6:** Output dictionary code for final remaining prefix $P$.
- **Step 7 [Decoding Loop]:** Initialize dictionary with 256 single-byte entries. Read first code, emit its string $S$, set `prev_str = S`.
- **Step 8:** For each subsequent code $k$: if $k$ exists in dictionary, entry $= dict[k]$; else special case $entry = prev\_str + prev\_str[0]$. Emit $entry$, insert $prev\_str + entry[0]$ into dictionary, update $prev\_str = entry$.
- **Step 9:** Reshape decoded byte stream to $M \times N$ and verify lossless fidelity.

---

## 4. Structured Pseudocode
```text
ALGORITHM LZWCompression(ByteSequence data):
    // 1. Initialize Dictionary with 256 single bytes
    dict = { bytes([i]): i FOR i = 0 TO 255 }
    next_code = 256
    
    P = b""
    codes = []

    FOR EACH byte IN data DO:
        C = bytes([byte])
        PC = P + C
        IF PC IN dict THEN:
            P = PC
        ELSE:
            codes.append(dict[P])
            dict[PC] = next_code
            next_code = next_code + 1
            P = C
        END IF
    END FOR
    IF P != b"" THEN:
        codes.append(dict[P])
    END IF

    RETURN codes
END ALGORITHM
```

---

## 5. Mathematical Formulations & Transformation Equations
- **Dictionary Expansion Rule:** $Dict[next\_code] = P \circ C \quad (next\_code \ge 256)$
- **Compression Ratio:** $CR = \frac{M \times N \times 8}{|codes| \times \lceil \log_2(next\_code) \rceil}$

---

## 6. Computational Complexity & Memory Footprint
- **Time Complexity:** $O(M \times N)$ linear execution using hash map dictionary lookups.
- **Space Complexity:** $O(D)$ where $D$ is total dictionary entries created.

---

## 7. Edge Cases & Boundary Handling
The classic LZW KwKwK decoding anomaly (code referenced before it is entered in decompressor dictionary) handled via $entry = prev\_str + prev\_str[0]$.

---

## 8. Viva Quick-Check: Key Algorithmic Invariants
- No dictionary transmitted: The decompressor rebuilds the identical dynamic dictionary strictly from the received code stream.
- Asymptotic optimality: LZW asymptotically converges to the finite-state entropy rate of the source.
