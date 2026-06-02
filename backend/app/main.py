from fastapi import FastAPI

app = FastAPI(
    title="MareMetrics API",
    description="AI-powered ocean data discovery platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to MareMetrics"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }