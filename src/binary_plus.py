"""
binary_plus.py  —  InfiniteOS φ-Code (Binary Plus)

Autor: Marta S. Reinhardt
Licença: MIT

Descrição:
Implementa o conceito de "Binary Plus" — um sistema numérico alternativo
baseado na razão áurea (φ ≈ 1.618) e nas proporções de Fibonacci.

Cada bit é substituído por uma unidade proporcional a φ^n, criando
camadas fractais de informação (multi-layer phi encoding).

"""

import math
from typing import List

# Constante da razão áurea
PHI = (1 + math.sqrt(5)) / 2  # ≈ 1.61803398875


# ----------------------------------------------------------
# Núcleo do Binary Plus
# ----------------------------------------------------------

def fibonacci(n: int) -> List[int]:
    """Gera os n primeiros números de Fibonacci (mínimo n=2)."""
        seq = [1, 1]
            for _ in range(2, n):
                    seq.append(seq[-1] + seq[-2])
                        return seq


                        def phi_encode(bits: List[int], layers: int = 3) -> List[float]:
                            """
                                Codifica uma sequência binária em camadas phi.
                                    - bits: lista de 0 e 1
                                        - layers: número de camadas fractais (1 = linear)
                                            Retorna lista de valores codificados.
                                                """
                                                    fib = fibonacci(len(bits) + layers)
                                                        encoded = []

                                                            for i, bit in enumerate(bits):
                                                                    if bit not in (0, 1):
                                                                                raise ValueError("Bits devem ser 0 ou 1.")
                                                                                        # peso phi em camadas: φⁿ * Fibonacci(i)
                                                                                                phi_weight = sum(PHI ** j for j in range(1, layers + 1))
                                                                                                        value = (PHI if bit == 1 else 1) * fib[i] * phi_weight
                                                                                                                encoded.append(round(value, 6))
                                                                                                                    return encoded


                                                                                                                    def phi_decode(encoded: List[float], threshold: float = PHI) -> List[int]:
                                                                                                                        """
                                                                                                                            Decodifica lista de valores phi em bits (0 ou 1),
                                                                                                                                usando limiar relativo à média/φ.
                                                                                                                                    """
                                                                                                                                        if not encoded:
                                                                                                                                                return []
                                                                                                                                                    avg = sum(encoded) / len(encoded)
                                                                                                                                                        return [1 if val >= avg / threshold else 0 for val in encoded]


                                                                                                                                                        def phi_layers(n: int) -> List[float]:
                                                                                                                                                            """Gera as potências de φ até n camadas."""
                                                                                                                                                                return [PHI ** i for i in range(1, n + 1)]


                                                                                                                                                                # ----------------------------------------------------------
                                                                                                                                                                # Exemplo de uso
                                                                                                                                                                # ----------------------------------------------------------
                                                                                                                                                                if __name__ == "__main__":
                                                                                                                                                                    bits = [1, 0, 1, 1, 0, 1]
                                                                                                                                                                        print("Bits originais:", bits)

                                                                                                                                                                            encoded = phi_encode(bits, layers=4)
                                                                                                                                                                                print("Codificado (φ-layers):", encoded)

                                                                                                                                                                                    decoded = phi_decode(encoded)
                                                                                                                                                                                        print("Decodificado:", decoded)

                                                                                                                                                                                            print("Camadas φ:", phi_layers(6))