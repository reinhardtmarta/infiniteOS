# system/trash.py
import os
import shutil

class TrashManager:
    def __init__(self, root="data/", trash_folder="trash/"):
            self.root = root
                    self.trash_folder = os.path.join(root, trash_folder)
                            os.makedirs(self.trash_folder, exist_ok=True)

                                def move_to_trash(self, filename):
                                        src = os.path.join(self.root, filename)
                                                dst = os.path.join(self.trash_folder, filename)
                                                        if os.path.exists(src):
                                                                    shutil.move(src, dst)
                                                                                return f"🗑️ '{filename}' moved to trash."
                                                                                        return f"⚠️ File '{filename}' not found."

                                                                                            def restore(self, filename):
                                                                                                    src = os.path.join(self.trash_folder, filename)
                                                                                                            dst = os.path.join(self.root, filename)
                                                                                                                    if os.path.exists(src):
                                                                                                                                shutil.move(src, dst)
                                                                                                                                            return f"♻️ '{filename}' restored."
                                                                                                                                                    return f"⚠️ File '{filename}' not found in trash."

                                                                                                                                                        def list_trash(self):
                                                                                                                                                                return os.listdir(self.trash_folder)
                                                                                                                                                                