import threading
import time
import logging
from openclaw.hub.store import JobStore
from openclaw.hub.scheduler import BinPackingScheduler

class Orchestrator:
    def __init__(self, store: JobStore):
        self.store = store
        self.scheduler = BinPackingScheduler()
        self.running = False
        self.logger = logging.getLogger("Orchestrator")

    def start(self):
        self.running = True
        threading.Thread(target=self._loop, daemon=True).start()
        self.logger.info("Orchestrator background thread started")

    def _loop(self):
        while self.running:
            try:
                self._reconcile()
            except Exception as e:
                self.logger.error(f"Error in reconciliation loop: {e}")
            time.sleep(5)

    def _reconcile(self):
        pending = self.store.list_jobs(status="pending")
        if not pending:
            return
            
        # Get active nodes (would come from Heartbeat server)
        nodes = {} 
        scheduled = self.scheduler.schedule(pending, nodes)
        # Update job statuses and trigger agent execution
