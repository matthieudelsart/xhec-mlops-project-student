#!/bin/bash
# Set Prefect API URL to be accessible at 0.0.0.0:4200
prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api

# Start Prefect server in the background
prefect server start --host 127.0.0.1 --port 4200 &

# Navigate to the correct directory
cd /web_service  # Make sure this path is correct

# Start FastAPI with Uvicorn on port 8001
uvicorn main:app --host 127.0.0.1 --port 8001
