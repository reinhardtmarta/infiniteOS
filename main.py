# main.py
# ==========================================
# 🌌 SO-Infinite v0.2
# Núcleo evolutivo baseado em φ (1.618)
# ==========================================

from kernel.core import InfiniteKernel
from kernel.protection import ProtectionLayer
from ui.shell import Shell
from time import sleep

def boot_sequence():
    print("🌀 Booting SO-Infinite v0.2 ...")
        sleep(0.5)
            print("⧉ Initializing Kernel ...")
                sleep(0.5)
                    print("⚙️  Loading subsystems ...")
                        sleep(0.5)
                            print("🔐 Security Layer active.\n")

                            if __name__ == "__main__":
                                boot_sequence()

                                    # Inicializa kernel e camada de proteção
                                        kernel = InfiniteKernel(mode="1 6 1 8")
                                            security = ProtectionLayer()

                                                # Evolui o kernel por algumas camadas
                                                    print("🧬 Kernel evolution:")
                                                        for _ in range(3):
                                                                layer = kernel.evolve()
                                                                        data = layer['description']
                                                                                sig = security.sign(layer['description'], data)
                                                                                        print(f"  ▪ {layer['description']} [sig: {sig[:8]}...]")
                                                                                                sleep(0.4)

                                                                                                    print("\n✅ All layers stable.")
                                                                                                        print("🚀 Launching interactive shell...\n")

                                                                                                            # Inicia o terminal interno
                                                                                                                shell = Shell()
                                                                                                                    shell.start()

                                                                                                                        print("\n🌙 System halted — SO-Infinite terminated safely.")