# OpenClaw Cluster Scheduler

An intelligent, fault-tolerant GPU cluster scheduler designed specifically for distributed deep learning training. OpenClaw leverages AI agents to handle resource allocation, job preemption, and automated recovery from hardware failures.

## Features

- **Distributed Training Support**: Optimized for PyTorch Distributed, JAX, and DeepSpeed.
- **Fault Tolerance**: Automatic detection of node failures and job rescheduling.
- **Intelligent Packing**: AI agents determine the best placement for jobs to minimize inter-node communication latency.
- **Priority Queuing**: Multi-user support with fair-share scheduling and job preemption.
- **Resource Monitoring**: Real-time tracking of GPU utilization, memory, and thermal metrics.

## Architecture

OpenClaw operates with a centralized controller (`the Hub`) and distributed agents (`the Sentinels`) running on each GPU node.

- **Orchestrator**: The core logic for job lifecycle management.
- **Scheduler**: Pluggable AI-driven scheduling algorithms.
- **Agent System**: Built on the OpenClaw Agent Framework to handle autonomous decision-making for cluster health.

## Installation

```bash
pip install openclaw-scheduler
```

## Basic Usage

### Starting the Hub

```bash
openclaw-hub --config config.yaml
```

### Submitting a Job

```python
from openclaw.client import Client

client = Client(hub_url="http://localhost:8080")

job_spec = {
    "name": "llama-7b-finetune",
    "image": "pytorch/pytorch:latest",
    "gpus": 8,
    "nodes": 2,
    "command": "python train.py --batch_size 32"
}

job_id = client.submit(job_spec)
print(f"Job submitted: {job_id}")
```

## License

MIT - See LICENSE file for details.
