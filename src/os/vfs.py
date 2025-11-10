# src/os/vfs.py
"""
Simple in-memory virtual filesystem (VFS) for InfiniteOS demo.
Not persistent — meant for demos / unit tests.
"""
from typing import Dict, Any

class VFS:
    def __init__(self):
            # path -> content (dict or string)
                    self.fs: Dict[str, Any] = {
                                "/": {}
                                        }

                                            def _split(self, path: str):
                                                    return [p for p in path.strip("/").split("/") if p]

                                                        def mkdir(self, path: str):
                                                                parts = self._split(path)
                                                                        node = self.fs["/"]
                                                                                for p in parts:
                                                                                            node = node.setdefault(p, {})
                                                                                                    return True

                                                                                                        def write(self, path: str, content: str):
                                                                                                                parts = self._split(path)
                                                                                                                        if not parts:
                                                                                                                                    raise ValueError("Cannot write to root")
                                                                                                                                            *dirs, name = parts
                                                                                                                                                    node = self.fs["/"]
                                                                                                                                                            for d in dirs:
                                                                                                                                                                        node = node.setdefault(d, {})
                                                                                                                                                                                node[name] = content
                                                                                                                                                                                        return True

                                                                                                                                                                                            def read(self, path: str):
                                                                                                                                                                                                    parts = self._split(path)
                                                                                                                                                                                                            node = self.fs["/"]
                                                                                                                                                                                                                    for p in parts:
                                                                                                                                                                                                                                if p not in node:
                                                                                                                                                                                                                                                raise FileNotFoundError(path)
                                                                                                                                                                                                                                                            node = node[p]
                                                                                                                                                                                                                                                                    if isinstance(node, dict):
                                                                                                                                                                                                                                                                                raise IsADirectoryError(path)
                                                                                                                                                                                                                                                                                        return node

                                                                                                                                                                                                                                                                                            def ls(self, path: str = "/"):
                                                                                                                                                                                                                                                                                                    parts = self._split(path)
                                                                                                                                                                                                                                                                                                            node = self.fs["/"]
                                                                                                                                                                                                                                                                                                                    for p in parts:
                                                                                                                                                                                                                                                                                                                                node = node.get(p, {})
                                                                                                                                                                                                                                                                                                                                        if isinstance(node, dict):
                                                                                                                                                                                                                                                                                                                                                    return list(node.keys())
                                                                                                                                                                                                                                                                                                                                                            return []