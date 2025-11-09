# system/process.py
import time

class Process:
    def __init__(self, name, action):
            self.name = name
                    self.action = action
                            self.status = "waiting"

                                def run(self):
                                        self.status = "running"
                                                time.sleep(0.5)  # Simula tempo de execução
                                                        result = self.action()
                                                                self.status = "done"
                                                                        return result

                                                                        class ProcessManager:
                                                                            def __init__(self):
                                                                                    self.queue = []

                                                                                        def add(self, process):
                                                                                                self.queue.append(process)

                                                                                                    def run_all(self):
                                                                                                            results = []
                                                                                                                    for p in self.queue:
                                                                                                                                results.append(p.run())
                                                                                                                                        return results