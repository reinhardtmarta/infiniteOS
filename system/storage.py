# system/storage.py
import os

class VirtualStorage:
    def __init__(self, root="data/"):
            self.root = root
                    os.makedirs(self.root, exist_ok=True)
                        
                            def create(self, name, content=""):
                                    path = os.path.join(self.root, name)
                                            with open(path, "w") as f:
                                                        f.write(content)
                                                                return f"File '{name}' created."
                                                                    
                                                                        def list_files(self):
                                                                                return os.listdir(self.root)