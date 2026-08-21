from fastapi import FastAPI

app = FastAPI(
    title="DevOps Demo Application",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Hello from Automated DevOps! Created by Sathvik M M DevSecOps Engineer",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }