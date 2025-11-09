# kernel/protection.py
import hashlib

class ProtectionLayer:
    def __init__(self):
            self.registry = {}

                def sign(self, name, data):
                        signature = hashlib.sha256(data.encode()).hexdigest()
                                self.registry[name] = signature
                                        return signature

                                            def verify(self, name, data):
                                                    new_sig = hashlib.sha256(data.encode()).hexdigest()
                                                            old_sig = self.registry.get(name)
                                                                    return old_sig == new_sig
                                                                    