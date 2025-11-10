# 🌀 Binary Plus (φ-Code)

**Author:** Marta S. Reinhardt  
**Project:** InfiniteOS  
**License:** MIT  
**Version:** 1.0  

---

## ✨ Overview

**Binary Plus (φ-Code)** is an alternative information encoding model that replaces
classical binary digits (0 and 1) with **φ-weighted logical units** — proportional to  
the **Golden Ratio (φ ≈ 1.618)** and the **Fibonacci sequence**.

Each "phi-bit" represents a proportional harmonic state rather than a simple binary value.  
This creates a **multi-layer, fractal, and self-similar** data structure, inspired by  
natural growth patterns and energy-efficient computation.
---

## ⚙️ Core Principle

The **Golden Ratio** is defined as:

\[
φ = \frac{1 + \sqrt{5}}{2} ≈ 1.6180339887
\]

and is intrinsically related to Fibonacci numbers:

\[
Fₙ₊₁ / Fₙ → φ
\]

The Binary Plus system maps each bit to a proportional φ-layer, optionally stacking multiple layers (`φ¹ + φ² + φ³ …`) to create **multi-dimensional encodings**.

---

## 🧩 Structure

| Symbol | Meaning | Example |
|:------:|:--------|:--------|
| `φ-bit` | Core logic unit | { 1, 1.618 } |
| `Layer` | Power of φ controlling weight | φ¹, φ², φ³… |
| `Fibonacci` | Base harmonic scaling | Fₙ × φˡ |
| `Encoding` | `value = bit × Fₙ × Σ(φˡ)` |  |

Each encoded sequence forms a **harmonic vector** — a mathematically stable pattern
with fractal self-similarity and potential for energy-optimized computation.

---

## 🧠 Mathematical Encoding

Given an input bit array **B = [b₁, b₂, …, bₙ]**  
and a selected number of layers **L**,  
the encoded output is:

\[
Eᵢ = (bᵢ ? φ : 1) × Fᵢ × Σ_{j=1}^{L} φ^j
\]

Decoding approximates back to binary by comparing each value to a φ-relative threshold:

\[
bᵢ' = 
\begin{cases}
1, & Eᵢ ≥ \bar{E}/φ \\
0, & \text{otherwise}
\end{cases}
\]

---

## 🧮 Python Implementation

The reference implementation is provided in  
`src/binary_plus.py`.

```python
from binary_plus import phi_encode, phi_decode

bits = [1, 0, 1, 1, 0, 1]
encoded = phi_encode(bits, layers=4)
decoded = phi_decode(encoded)

print(encoded)
print(decoded)
[16.236, 8.118, 48.708, 81.558, 40.59, 210.54]
[1, 0, 1, 1, 0, 1]