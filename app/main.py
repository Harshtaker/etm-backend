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
from fastapi import FastAPI
from app.routes.buses import router as bus_router

app = FastAPI()

app.include_router(bus_router)
from app.routes.users import router as user_router

app.include_router(user_router)
