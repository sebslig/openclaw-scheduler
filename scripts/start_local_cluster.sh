#!/bin/bash
# Mock script to simulate a multi-node training environment
echo "Launching OpenClaw Hub..."
export HUB_URL="http://localhost:8080"
python3 -m openclaw.hub.main &

sleep 2

echo "Launching Sentinel Agent..."
export NODE_ID="gpu-node-01"
python3 -m openclaw.agent.main &

echo "Cluster is ready."
wait
