# SO-Infinite Instruction Set Architecture (ISA)
**Version:** v0.1-spec  
**Concept:** 1 · 6 · 1 · 8 — genesis, expansion, return, transcendence.  
**Cell base:** multivalued cell 0–15 (4 logical bits, optional φ-weighting).

---

## 1. Physical and logical structure

| Element | Description |
|---------|-------------|
| **Cell** | Smallest data unit (4 bits). Each cell has value `v ∈ [0,15]` and optional φ-weight. |
| **Word** | Group of 8 cells (32 physical bits). |
| **Memory** | Linear array of cells, addressed by cell index. |
| **Registers** | R0–R7 (8 general-purpose registers). |
| **Mode** | MODE ∈ {1, 6, 8} — alters instruction semantics. |
| **PC** | Program Counter (instruction index). |
| **Φ (phi)** | Constant 1.61803398875 used for weighted operations.

---

## 2. Instruction format

Each instruction is 4 bytes:  
`[OPCODE] [A] [B] [C]`

- **OPCODE:** numeric code for operation.  
- **A, B, C:** registers or cell addresses (operand encoding decided by assembler).

---

## 3. Basic instruction set

| Name | Opcode | Description |
|------|--------|-------------|
| `NOP` | `0x00` | No operation. |
| `LOAD r, addr` | `0x10` | Load cell from memory into register. |
| `STORE r, addr` | `0x11` | Store register value into memory cell. |
| `MOV r1, r2` | `0x12` | Copy register value. |
| `ADD_MV r1, r2, r3` | `0x20` | Multivalued add: r1 = MV_ADD(r2, r3). |
| `MUL_MV r1, r2, imm` | `0x21` | Multivalued multiply: r1 = MV_MUL(r2, imm). |
| `COLLAPSE r, addr` | `0x30` | Collapse cell value to binary (0/1) into register. |
| `SPAWN r, addr` | `0x40` | Create a new cell derived from addr (mode 8 behavior). |
| `SIGN r, addr` | `0x50` | Create an integrity signature/hash for data. |
| `BRZ r, off` | `0x60` | Branch if register is zero (offset). |
| `JMP off` | `0x61` | Unconditional jump. |
| `SETMODE imm` | `0x70` | Set execution mode (1, 6, or 8). |
| `HALT` | `0xFF` | Stop execution. |

---

## 4. Multivalued operation rules (MV)

- `MV_ADD(a, b)` = `round((a + b) / φ)` when `MODE == 6`; otherwise `(a + b) % 16`.
- `MV_MUL(a, k)` = `min(15, round(a * k))`.
- `COLLAPSE(v)` = `1 if v >= 8 else 0` (threshold collapse; can be tuned).

---

## 5. Mode effects

The machine keeps a `MODE` register. Mode affects arithmetic and structural operations:

- `MODE = 1` (Genesis / identity): direct semantics, read/write straightforward.
- `MODE = 6` (Expansion): arithmetic uses φ-weighting; MV ops smooth and propagate.
- `MODE = 8` (Transcendence): enables parallel/replication primitives (SPAWN, block ops).

---

## 6. Execution flow

1. Boot sequence sets `MODE = 1`.
2. Interpreter fetches and decodes instructions sequentially.
3. Operations respect current `MODE`.
4. `HALT` triggers optional memory dump (a “soul dump”) for analysis.

---

## 7. Example program (symbolic assembly)

; Demo: read, expand, collapse, sign SETMODE 1 LOAD R1, 0x00 MOV R2, R1 SETMODE 6 ADD_MV R3, R1, R2 STORE R3, 0x10 SETMODE 1 COLLAPSE R4, 0x10 SIGN R4, 0x10 HALT

---

## 8. Future extensions

- FPGA/HDL layer — cells mapped to 4-bit registers with φ-weighting logic.
- Rust runtime and LLVM backend for native performance.
- Parallel VM and hardware acceleration for `MODE=8` operations.