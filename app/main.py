from fastapi import FastAPI
from app.database import engine, Base
from app.routes import buses_router, drivers_router, users_router, feedback_router, tracking_router
from app.routes.bus_stops import router as bus_stops_router

# Initialize FastAPI app
app = FastAPI(title="ETM Bus Tracking API 🚍")

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Include all routers
app.include_router(buses_router)
app.include_router(drivers_router)
app.include_router(users_router)
app.include_router(feedback_router)
app.include_router(tracking_router)
app.include_router(bus_stops_router)  # <-- include after app is created

# Health check
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "ETM Bus Tracking API is running!"}

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to ETM Bus Tracking API 🚍"}
