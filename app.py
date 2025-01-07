from fastapi import FastAPI

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return {
        "version": "1.0.0",
        "description": "FastAPI REST API"
    }
