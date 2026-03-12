import requests
from openclaw.core.models import JobSpec

class Client:
    def __init__(self, hub_url: str):
        self.hub_url = hub_url.rstrip("/")

    def submit(self, spec_dict: dict) -> str:
        # Validate through JobSpec
        spec = JobSpec(**spec_dict)
        resp = requests.post(f"{self.hub_url}/jobs", json=spec.dict())
        resp.raise_for_status()
        return resp.json()["job_id"]

    def get_status(self, job_id: str) -> dict:
        resp = requests.get(f"{self.hub_url}/jobs/{job_id}")
        resp.raise_for_status()
        return resp.json()
