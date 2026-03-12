import unittest
from openclaw.hub.store import JobStore
from openclaw.core.models import JobSpec, ResourceRequest

class TestJobStore(unittest.TestCase):
    def test_job_creation(self):
        store = JobStore()
        spec = JobSpec(
            name="test-job",
            image="test-image",
            command="echo 1",
            resources_per_node=ResourceRequest(gpus=1)
        )
        job_id = store.create_job(spec)
        job = store.get_job(job_id)
        self.assertEqual(job.spec.name, "test-job")
        self.assertEqual(len(store.list_jobs()), 1)

if __name__ == "__main__":
    unittest.main()
