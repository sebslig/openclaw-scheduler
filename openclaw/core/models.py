from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from enum import Enum

class JobStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    PREEMPTED = "preempted"

class ResourceRequest(BaseModel):
    gpus: int = 1
    cpu_cores: int = 4
    memory_gb: int = 16

class JobSpec(BaseModel):
    name: str
    image: str
    command: str
    nodes: int = 1
    resources_per_node: ResourceRequest
    env_vars: Dict[str, str] = {}
    priority: int = 0

class JobRecord(BaseModel):
    job_id: str
    spec: JobSpec
    status: JobStatus
    assigned_nodes: List[str] = []
    created_at: float
    updated_at: float
