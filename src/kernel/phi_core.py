"""
phi_core.py — InfiniteOS Kernel Layer (φ-Core Integration)

This module integrates the Binary Plus (φ-Code) logic directly into
the InfiniteOS kernel. It provides harmonic encoding, decoding, and
state management across multi-layer φ-based computation.

Author: Marta S. Reinhardt
License: MIT
"""

from src.modules.binary_plus import phi_encode, phi_decode, PHI

class PhiCore:
    """
        The central harmonic logic kernel.
            Uses φ (1.618) as the proportional constant for logic propagation.
                """

                    def __init__(self, layers: int = 4):
                            self.layers = layers
                                    self.state = []
                                            self.memory = []

                                                # -------------------------------------------------------------
                                                    # Core encoding and decoding
                                                        # -------------------------------------------------------------
                                                            def encode(self, bits):
                                                                    """Encode a binary vector into φ-space."""
                                                                            encoded = phi_encode(bits, self.layers)
                                                                                    self.state = encoded
                                                                                            self.memory.append(encoded)
                                                                                                    return encoded

                                                                                                        def decode(self):
                                                                                                                """Decode the current φ-state back to binary logic."""
                                                                                                                        if not self.state:
                                                                                                                                    return []
                                                                                                                                            return phi_decode(self.state)

                                                                                                                                                # -------------------------------------------------------------
                                                                                                                                                    # Adaptive harmonics
                                                                                                                                                        # -------------------------------------------------------------
                                                                                                                                                            def harmonize(self):
                                                                                                                                                                    """
                                                                                                                                                                            Apply harmonic normalization:
                                                                                                                                                                                    adjusts φ layers based on feedback and energy balance.
                                                                                                                                                                                            """
                                                                                                                                                                                                    if not self.state:
                                                                                                                                                                                                                return []

                                                                                                                                                                                                                        avg = sum(self.state) / len(self.state)
                                                                                                                                                                                                                                harmonized = [round(v / avg * PHI, 6) for v in self.state]
                                                                                                                                                                                                                                        self.state = harmonized
                                                                                                                                                                                                                                                return harmonized

                                                                                                                                                                                                                                                    # -------------------------------------------------------------
                                                                                                                                                                                                                                                        # Debug / inspection
                                                                                                                                                                                                                                                            # -------------------------------------------------------------
                                                                                                                                                                                                                                                                def info(self):
                                                                                                                                                                                                                                                                        return {
                                                                                                                                                                                                                                                                                    "layers": self.layers,
                                                                                                                                                                                                                                                                                                "current_state": self.state,
                                                                                                                                                                                                                                                                                                            "φ": PHI,
                                                                                                                                                                                                                                                                                                                        "memory_depth": len(self.memory),
                                                                                                                                                                                                                                                                                                                                }


                                                                                                                                                                                                                                                                                                                                # -------------------------------------------------------------
                                                                                                                                                                                                                                                                                                                                # Example usage (can be removed in production)
                                                                                                                                                                                                                                                                                                                                # -------------------------------------------------------------
                                                                                                                                                                                                                                                                                                                                if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                    core = PhiCore(layers=5)
                                                                                                                                                                                                                                                                                                                                        bits = [1, 0, 1, 1, 0, 1]
                                                                                                                                                                                                                                                                                                                                            print("Input bits:", bits)

                                                                                                                                                                                                                                                                                                                                                encoded = core.encode(bits)
                                                                                                                                                                                                                                                                                                                                                    print("Encoded φ:", encoded)

                                                                                                                                                                                                                                                                                                                                                        core.harmonize()
                                                                                                                                                                                                                                                                                                                                                            print("Harmonized φ:", core.state)

                                                                                                                                                                                                                                                                                                                                                                decoded = core.decode()
                                                                                                                                                                                                                                                                                                                                                                    print("Decoded bits:", decoded)

                                                                                                                                                                                                                                                                                                                                                                        print("Kernel info:", core.info())