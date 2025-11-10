# main.py
# ==========================================
# 🌌 SO-Infinite v0.4
# Núcleo evolutivo baseado em φ (1.618)
# ==========================================

from time import sleep
from kernel.core import InfiniteKernel
from kernel.protection import ProtectionLayer
from ui.shell import Shell
from src.kernel.phi_core import PhiCore


def boot_sequence():
    print("🌀 Booting SO-Infinite v0.4 ...")
        sleep(0.5)
            print("⧉ Initializing Kernel ...")
                sleep(0.5)
                    print("⚙️  Loading subsystems ...")
                        sleep(0.5)
                            print("🔐 Security Layer active.\n")


                            if __name__ == "__main__":
                                boot_sequence()

                                    # Inicializa o núcleo e a camada de proteção
                                        kernel = InfiniteKernel(mode="1 6 1 8")
                                            security = ProtectionLayer()

                                                # Teste simbólico com o núcleo φ
                                                    bits = [1, 0, 1, 1, 0, 1]
                                                        core = PhiCore(layers=4)
                                                            encoded = core.encode(bits)
                                                                print("Encoded:", encoded)
                                                                    harmonized = core.harmonize()
                                                                        print("Harmonized:", harmonized)
                                                                            decoded = core.decode()
                                                                                print("Decoded:", decoded)

                                                                                    # Evolui o kernel
                                                                                        print("\n🧬 Kernel evolution:")
                                                                                            for _ in range(3):
                                                                                                    layer = kernel.evolve()
                                                                                                            data = layer["description"]
                                                                                                                    sig = security.sign(layer["description"], data)
                                                                                                                            print(f"  ▪ {layer['description']} [sig: {sig[:8]}...]")
                                                                                                                                    sleep(0.4)

                                                                                                                                        print("\n✅ All layers stable.")
                                                                                                                                            print("🚀 Launching interactive shell...\n")

                                                                                                                                                # Inicia o terminal interno
                                                                                                                                                    shell = Shell()
                                                                                                                                                        shell.start()

                                                                                                                                                            # Roda o scheduler harmônico do kernel
                                                                                                                                                                kernel.run(runtime=3.0)

                                                                                                                                                                    print("\n🌙 System halted — SO-Infinite terminated safely.")