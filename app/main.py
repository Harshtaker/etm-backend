from fastapi import FastAPI
from app.routes import router as bus_router

app = FastAPI(title="ETM Backend 🚍")

app.include_router(bus_router)

@app.get("/")
def root():
    return {"message": "ETM Backend is running 🚍"}
