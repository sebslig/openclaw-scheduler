import time
import uuid
from typing import List, Dict
from openclaw.core.models import JobSpec, JobRecord, JobStatus

class JobStore:
    def __init__(self):
        self.jobs: Dict[str, JobRecord] = {}

    def create_job(self, spec: JobSpec) -> str:
        job_id = str(uuid.uuid4())
        record = JobRecord(
            job_id=job_id,
            spec=spec,
            status=JobStatus.PENDING,
            created_at=time.time(),
            updated_at=time.time()
        )
        self.jobs[job_id] = record
        return job_id

    def get_job(self, job_id: str) -> JobRecord:
        return self.jobs.get(job_id)

    def list_jobs(self, status: JobStatus = None) -> List[JobRecord]:
        if status:
            return [j for j in self.jobs.values() if j.status == status]
        return list(self.jobs.values())

    def update_status(self, job_id: str, status: JobStatus):
        if job_id in self.jobs:
            self.jobs[job_id].status = status
            self.jobs[job_id].updated_at = time.time()
