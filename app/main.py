from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI()

REQUEST_COUNT = Counter(
    "api_requests_total",
    "Total number of API requests"
)


@app.get("/")
def root():
    REQUEST_COUNT.inc()

    return {
        "message": "Kubernetes Platform Lab",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/ready")
def ready():
    return {"status": "ready"}


@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )