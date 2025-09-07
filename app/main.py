from fastapi import FastAPI
from app.database import Base, engine
from app.routes import users, buses, tickets, drivers, feedback # make sure file is feedbacks.py

# Create DB tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app with metadata
app = FastAPI(
    title="ETM Backend 🚍",
    description="Backend service for Electronic Ticketing Machines (ETM).",
    version="1.0.0"
)

# Include routers with prefixes and tags
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(buses.router, prefix="/buses", tags=["Buses"])
app.include_router(tickets.router, prefix="/tickets", tags=["Tickets"])
app.include_router(drivers.router, prefix="/drivers", tags=["Drivers"])
app.include_router(feedback.router, prefix="/feedbacks", tags=["Feedbacks"])

# Root endpoint
@app.get("/", tags=["System"], summary="Root")
def root():
    """Root endpoint to check if backend is running."""
    return {"message": "ETM Backend is running 🚍"}

# Health check endpoint
@app.get("/healthz", tags=["System"], summary="Health Check")
def health():
    """Health check endpoint for uptime monitoring."""
    return {"status": "ok"}
