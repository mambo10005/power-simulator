from fastapi import FastAPI

app = FastAPI(
    title="Power Simulator"
)

@app.get("/")
def root():

    return {
        "message": "Power Simulator API"
    }

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }