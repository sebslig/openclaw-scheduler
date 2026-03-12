import os
import subprocess
import logging
from openclaw.core.models import JobSpec

class ProcessManager:
    def __init__(self):
        self.logger = logging.getLogger("ProcessManager")
        self.active_processes = {}

    def run_job(self, job_id: str, spec: JobSpec):
        self.logger.info(f"Starting job {job_id}: {spec.command}")
        
        # Simplified execution logic
        try:
            proc = subprocess.Popen(
                spec.command.split(),
                env={**os.environ, **spec.env_vars},
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            self.active_processes[job_id] = proc
        except Exception as e:
            self.logger.error(f"Failed to launch job {job_id}: {e}")

    def stop_job(self, job_id: str):
        if job_id in self.active_processes:
            proc = self.active_processes[job_id]
            proc.terminate()
            del self.active_processes[job_id]
