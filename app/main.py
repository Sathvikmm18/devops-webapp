from fastapi import FastAPI

app = FastAPI(
    title="DevOps Demo Application",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Hello from DevOps! Created by Sathvik M M",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy All is well"
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }