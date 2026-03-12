import time
import logging
import psutil
from typing import Dict

class NodeMonitor:
    def __init__(self):
        self.logger = logging.getLogger("NodeMonitor")

    def get_stats(self) -> Dict:
        # In a real scenario, use pynvml here for GPU stats
        stats = {
            "cpu_percent": psutil.cpu_percent(),
            "mem_percent": psutil.virtual_memory().percent,
            "gpu_count": 0, # Placeholder
            "timestamp": time.time()
        }
        return stats

    def check_health(self) -> bool:
        # Logic to check if node is healthy (OOMs, GPU errors, etc.)
        return True
