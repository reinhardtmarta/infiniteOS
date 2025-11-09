# kernel/core.py
from math import sqrt

class InfiniteKernel:
    def __init__(self, mode="1 6 1 8"):
            self.mode = mode
                    self.layers = []
                            self.step = 0
                                
                                    def evolve(self):
                                            phi = (1 + sqrt(5)) / 2
                                                    self.step += 1
                                                            layer = {
                                                                            "id": self.step,
                                                                                        "growth": round(phi ** self.step, 3),
                                                                                                    "description": f"Layer {self.step} active – Mode {self.mode}"
                                                            }
                                                                    self.layers.append(layer)
                                                                            return layer
                                                                                
                                                                                    def status(self):
                                                                                            return [f"{l['id']}: {l['description']}" for l in self.layers]
                                                            }