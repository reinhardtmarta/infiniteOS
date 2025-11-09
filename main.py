# main.py
from kernel.core import InfiniteKernel
from system.storage import VirtualStorage

if __name__ == "__main__":
    kernel = InfiniteKernel()
        storage = VirtualStorage()
            
                print("🌀 SO-Infinite Booting...\n")
                    
                        for _ in range(3):
                                layer = kernel.evolve()
                                        print(layer)
                                            
                                                storage.create("welcome.txt", "Welcome to SO-Infinite")
                                                    print("\nFiles:", storage.list_files())
                                                    