"""
storage.py — Harmonic Virtual File System (VFS)
===============================================

Responsável por armazenar e recuperar o estado do SO-Infinite
de forma simbiótica com o φ-Core. Utiliza JSON para persistência
e codificação harmônica (Binary Plus) para compressão leve.

Autor: Marta S. Reinhardt
Licença: MIT
"""

import json
import os
from datetime import datetime
from src.kernel.phi_core import phi_encode, phi_decode

# Diretório padrão de armazenamento
VFS_PATH = "system_data/"
STATE_FILE = os.path.join(VFS_PATH, "infinite_state.json")


class HarmonicStorage:
    """
        Sistema de persistência harmônico baseado em JSON + φ.
            """

                def __init__(self):
                        os.makedirs(VFS_PATH, exist_ok=True)

                            # -----------------------------------------------------
                                # Funções básicas de persistência
                                    # -----------------------------------------------------
                                        def save_state(self, state_data: dict):
                                                """
                                                        Salva o estado atual do sistema em formato JSON harmônico.
                                                                """
                                                                        encoded_state = self._harmonic_encode(state_data)
                                                                                with open(STATE_FILE, "w", encoding="utf-8") as f:
                                                                                            json.dump(encoded_state, f, indent=2)
                                                                                                    print(f"💾 Estado salvo com sucesso ({STATE_FILE}).")

                                                                                                        def load_state(self) -> dict:
                                                                                                                """
                                                                                                                        Carrega o estado salvo, se existir.
                                                                                                                                """
                                                                                                                                        if not os.path.exists(STATE_FILE):
                                                                                                                                                    print("⚠️ Nenhum estado salvo encontrado.")
                                                                                                                                                                return {}

                                                                                                                                                                        with open(STATE_FILE, "r", encoding="utf-8") as f:
                                                                                                                                                                                    encoded_state = json.load(f)

                                                                                                                                                                                            state = self._harmonic_decode(encoded_state)
                                                                                                                                                                                                    print(f"📂 Estado restaurado ({STATE_FILE}).")
                                                                                                                                                                                                            return state

                                                                                                                                                                                                                # -----------------------------------------------------
                                                                                                                                                                                                                    # Codificação harmônica (φ)
                                                                                                                                                                                                                        # -----------------------------------------------------
                                                                                                                                                                                                                            def _harmonic_encode(self, data):
                                                                                                                                                                                                                                    """
                                                                                                                                                                                                                                            Converte dados binários em φ-camadas para compressão simbólica.
                                                                                                                                                                                                                                                    """
                                                                                                                                                                                                                                                            try:
                                                                                                                                                                                                                                                                        # Gera um padrão numérico simples a partir do dicionário
                                                                                                                                                                                                                                                                                    bits = [1 if ord(c) % 2 == 0 else 0 for c in str(data)]
                                                                                                                                                                                                                                                                                                phi_layers = phi_encode(bits, layers=3)
                                                                                                                                                                                                                                                                                                            return {"phi_layers": phi_layers, "data": data, "timestamp": str(datetime.now())}
                                                                                                                                                                                                                                                                                                                    except Exception as e:
                                                                                                                                                                                                                                                                                                                                print("Erro ao codificar:", e)
                                                                                                                                                                                                                                                                                                                                            return {"data": data}

                                                                                                                                                                                                                                                                                                                                                def _harmonic_decode(self, encoded):
                                                                                                                                                                                                                                                                                                                                                        """
                                                                                                                                                                                                                                                                                                                                                                Decodifica dados φ de volta para o formato original.
                                                                                                                                                                                                                                                                                                                                                                        """
                                                                                                                                                                                                                                                                                                                                                                                try:
                                                                                                                                                                                                                                                                                                                                                                                            if "phi_layers" in encoded:
                                                                                                                                                                                                                                                                                                                                                                                                            phi_decode(encoded["phi_layers"])
                                                                                                                                                                                                                                                                                                                                                                                                                        return encoded.get("data", {})
                                                                                                                                                                                                                                                                                                                                                                                                                                except Exception as e:
                                                                                                                                                                                                                                                                                                                                                                                                                                            print("Erro ao decodificar:", e)
                                                                                                                                                                                                                                                                                                                                                                                                                                                        return encoded


                                                                                                                                                                                                                                                                                                                                                                                                                                                        # -----------------------------------------------------
                                                                                                                                                                                                                                                                                                                                                                                                                                                        # Teste rápido
                                                                                                                                                                                                                                                                                                                                                                                                                                                        # -----------------------------------------------------
                                                                                                                                                                                                                                                                                                                                                                                                                                                        if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                                                                                                                                            vfs = HarmonicStorage()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                sample_state = {
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        "version": "0.3",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                "kernel_mode": "1 6 1 8",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        "memory_layers": 3,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                "uptime": "42 cycles"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    }

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        vfs.save_state(sample_state)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            restored = vfs.load_state()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print("🔄 Estado restaurado:", restored)