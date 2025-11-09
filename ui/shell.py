# ui/shell.py
from system.storage import VirtualStorage
from system.trash import TrashManager

class Shell:
    def __init__(self):
            self.storage = VirtualStorage()
                    self.trash = TrashManager()

                        def start(self):
                                print("SO-Infinite Shell v0.1 — type 'help' for commands")
                                        while True:
                                                    cmd = input("∞ > ").strip().lower()
                                                                if cmd == "exit":
                                                                                print("🌀 Exiting shell...")
                                                                                                break
                                                                                                            elif cmd == "help":
                                                                                                                            print("Commands: ls, create <name>, del <name>, trash, restore <name>, exit")
                                                                                                                                        elif cmd == "ls":
                                                                                                                                                        print(self.storage.list_files())
                                                                                                                                                                    elif cmd.startswith("create "):
                                                                                                                                                                                    name = cmd.split(" ", 1)[1]
                                                                                                                                                                                                    print(self.storage.create(name, "Empty file"))
                                                                                                                                                                                                                elif cmd.startswith("del "):
                                                                                                                                                                                                                                name = cmd.split(" ", 1)[1]
                                                                                                                                                                                                                                                print(self.trash.move_to_trash(name))
                                                                                                                                                                                                                                                            elif cmd == "trash":
                                                                                                                                                                                                                                                                            print(self.trash.list_trash())
                                                                                                                                                                                                                                                                                        elif cmd.startswith("restore "):
                                                                                                                                                                                                                                                                                                        name = cmd.split(" ", 1)[1]
                                                                                                                                                                                                                                                                                                                        print(self.trash.restore(name))
                                                                                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                                                                                    print("❓ Unknown command.")