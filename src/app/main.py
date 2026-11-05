import os

from fastapi import FastAPI

app = FastAPI(title="e2e-p-11051145-2")


@app.get("/")
def root() -> dict:
    return {
        "service": os.environ.get("SERVICE_NAME", "e2e-p-11051145-2"),
        "description": "auto run 2",
    }


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
