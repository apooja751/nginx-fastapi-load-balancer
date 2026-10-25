
import os
import socket
from fastapi import FastAPI

app = FastAPI(
    title="Nginx FastAPI Load Balancer",
    description="Demonstration of load balancing across two FastAPI instances",
    version="1.0.0",
)

INSTANCE_ID = os.getenv("INSTANCE_ID", socket.gethostname())


@app.get("/")
def home():
    return {
        "message": "FastAPI application is running!",
        "instance": INSTANCE_ID,
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "instance": INSTANCE_ID,
    }
