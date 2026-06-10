from fastapi import FastAPI

app = FastAPI(title="FastAPI CI/CD Demo")


@app.get("/")
def root():
    return {"message": "FastAPI CI/CD Demo is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/version")
def version():
    return {"version": "1.0.0"}


@app.get("/environment")
def environment():
    return {"environment": "development"}


