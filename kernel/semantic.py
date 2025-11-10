# kernel/semantic.py
import math

class SemanticLayer:
    def __init__(self):
            self.dictionary = {
                        0: "void",
                                    1: "presence",
                                                1.618: "harmony",
                                                            2.618: "growth"
                                                                    }

                                                                        def interpret(self, pattern):
                                                                                """Converte padrões numéricos em significado simbólico"""
                                                                                        return [self.dictionary.get(round(v, 3), "unknown") for v in pattern]

                                                                                            def synthesize(self, words):
                                                                                                    """Transforma conceitos simbólicos de volta em código harmônico"""
                                                                                                            reverse = {v: k for k, v in self.dictionary.items()}
                                                                                                                    return [reverse.get(w, 0.0) for w in words]

                                                                                                                        def evolve(self, feedback):
                                                                                                                                """Ajusta o dicionário com base na experiência"""
                                                                                                                                        for k, v in feedback.items():
                                                                                                                                                    self.dictionary[k] = v