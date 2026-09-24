
import os

from fastapi import FastAPI

APP_VERSION = "1.0.1"
APP_ENV = os.getenv("APP_ENV", "development")
APP_REGION = os.getenv("APP_REGION", "local")

app = FastAPI(
    title="Capstone Documentation Demo API",
    description="A small FAST API used to test automated technical documentation generation.",
    version=APP_VERSION,
)


@app.get("/health", tags=["system"])
def health_check():
    return {
        "status": "ok",
        "environment": APP_ENV,
    }


@app.get("/hello/{name}", tags=["greetings"])
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/version", tags=["system"])
def get_version():
    return {
        "version": APP_VERSION,
        "environment": APP_ENV,
        "region": APP_REGION,
    }
