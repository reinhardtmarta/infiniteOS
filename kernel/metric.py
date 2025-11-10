# kernel/metric.py
# ==========================================
# 🔱 Phi Metric - Harmonic evaluation system
# ==========================================

class PhiMetric:
    def __init__(self, phi=1.618):
            self.phi = phi

                def evaluate(self, value):
                        """Return harmonic alignment score (0–1)"""
                                deviation = abs(value - self.phi)
                                        score = max(0.0, round(1 - deviation, 3))
                                                return score

                                                    def batch(self, values):
                                                            """Evaluate a list of values"""
                                                                    if not values:
                                                                                return 0.0
                                                                                        scores = [self.evaluate(v) for v in values]
                                                                                                avg = round(sum(scores) / len(scores), 3)
                                                                                                        return avg