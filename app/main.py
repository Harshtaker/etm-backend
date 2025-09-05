from fastapi import FastAPI
from app.routes import router as bus_router

app = FastAPI(title="ETM Backend 🚍")

app.include_router(bus_router)

@app.get("/")
def root():
    return {"message": "ETM Backend is running 🚍"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/healthz")
def health():
    return {"status": "ok"}
