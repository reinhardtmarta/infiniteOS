
# src/os/init.py
"""
Init process: starts basic services and a CLI demo.
"""
import time
from src.os.vfs import VFS

def simple_service(proc):
    # exemplo de serviço que registra timestamp no VFS
        vfs = proc.context.setdefault("vfs", VFS())
            for i in range(3):
                    path = f"/service/log_{proc.pid}_{i}.txt"
                            vfs.write(path, f"tick {i} from service {proc.pid} at {time.time()}")
                                    time.sleep(0.5)
                                        print(f"[{proc.name}] service finished.")

                                        def cli_process(proc):
                                            # CLI demo que usa PhiCore via proc.context['kernel']
                                                kernel = proc.context.get("kernel")
                                                    if kernel is None:
                                                            print(f"[{proc.name}] no kernel context found.")
                                                                    return

                                                                        print("InfiniteOS CLI (type 'help')\n")
                                                                            # demo loop  — em um TTY real, seria blocking; aqui apenas 3 comandos de demo
                                                                                commands = ["help", "phi encode 1011", "phi harmonize", "exit"]
                                                                                    for cmd in commands:
                                                                                            print(f"> {cmd}")
                                                                                                    parts = cmd.split()
                                                                                                            if parts[0] == "help":
                                                                                                                        print("commands: help | phi encode <bits> | phi harmonize | exit")
                                                                                                                                elif parts[0] == "phi" and parts[1] == "encode":
                                                                                                                                            bits = [int(c) for c in parts[2].strip()]
                                                                                                                                                        encoded = kernel.encode_state(bits)
                                                                                                                                                                    print("encoded:", encoded)
                                                                                                                                                                            elif parts[0] == "phi" and parts[1] == "harmonize":
                                                                                                                                                                                        print("harmonized:", kernel.harmonize())
                                                                                                                                                                                                elif parts[0] == "exit":
                                                                                                                                                                                                            print("CLI exiting.")
                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                time.sleep(0.4)

                                                                                                                                                                                                                                def init_process(kernel):
                                                                                                                                                                                                                                    """
                                                                                                                                                                                                                                        Function that the kernel can spawn as PID 1.
                                                                                                                                                                                                                                            """
                                                                                                                                                                                                                                                def _proc(proc):
                                                                                                                                                                                                                                                        # attach kernel reference to context so child services can use phi
                                                                                                                                                                                                                                                                proc.context["kernel"] = kernel
                                                                                                                                                                                                                                                                        # spawn a simple background service
                                                                                                                                                                                                                                                                                kernel.spawn(simple_service, name="svc")
                                                                                                                                                                                                                                                                                        # run CLI (blocking demo)
                                                                                                                                                                                                                                                                                                cli_process(proc)
                                                                                                                                                                                                                                                                                                    return _proc