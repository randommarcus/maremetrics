from fastapi import FastAPI

from app.routes.argovis import router as argovis_router

app = FastAPI(
    title="MareMetrics API"
)

app.include_router(argovis_router)


@app.get("/")
def root():
    return {
        "message": "MareMetrics API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }