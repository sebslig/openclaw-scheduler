import uvicorn
from fastapi import FastAPI, HTTPException
from openclaw.core.models import JobSpec, JobRecord
from openclaw.hub.store import JobStore
from openclaw.hub.engine import Orchestrator

app = FastAPI(title="OpenClaw Hub")
store = JobStore()
engine = Orchestrator(store)

@app.on_event("startup")
async def startup():
    engine.start()

@app.post("/jobs")
async def submit_job(spec: JobSpec):
    job_id = store.create_job(spec)
    return {"job_id": job_id}

@app.get("/jobs/{job_id}")
async def get_job(job_id: str):
    job = store.get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

def main():
    uvicorn.run(app, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()
