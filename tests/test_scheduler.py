import unittest
from openclaw.hub.scheduler import BinPackingScheduler
from openclaw.core.models import JobRecord, JobSpec, ResourceRequest, JobStatus
import time

class TestScheduler(unittest.TestCase):
    def test_scheduling_priority(self):
        scheduler = BinPackingScheduler()
        spec = JobSpec(
            name="prio-job", 
            image="img", 
            command="ls", 
            priority=10,
            resources_per_node=ResourceRequest()
        )
        job = JobRecord(
            job_id="1", 
            spec=spec, 
            status=JobStatus.PENDING, 
            created_at=time.time(), 
            updated_at=time.time()
        )
        
        # Simple test to ensure scheduler entry point runs without error
        scheduled = scheduler.schedule([job], {})
        self.assertIsInstance(scheduled, list)

if __name__ == "__main__":
    unittest.main()
