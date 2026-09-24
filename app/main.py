import os

from fastapi import FastAPI

app = FastAPI(
    title="Capstone Documentation Demo API",
    description="A small API used to test automated technical documentation generation.",
    version="1.0.0",
)

APP_ENV = os.getenv("APP_ENV", "development")


@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok", "environment": APP_ENV}


@app.get("/hello/{name}", tags=["greetings"])
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
