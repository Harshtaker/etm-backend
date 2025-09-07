from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import SessionLocal, redis_client
from app.models import Bus
from app.schemas.bus import BusCreate, BusResponse, BusLocationUpdate
import json

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST /bus/ → Add new bus
@router.post("/bus/", response_model=BusResponse)
def create_bus(bus: BusCreate, db: Session = Depends(get_db)):
    db_bus = Bus(**bus.dict())
    db.add(db_bus)
    db.commit()
    db.refresh(db_bus)

    redis_client.hset("buses", db_bus.id, json.dumps({
        "bus_number": db_bus.bus_number,
        "latitude": db_bus.latitude,
        "longitude": db_bus.longitude
    }))
    return db_bus

# GET /bus/ → Get all buses
@router.get("/bus/", response_model=list[BusResponse])
def get_buses(db: Session = Depends(get_db)):
    buses = []
    redis_buses = redis_client.hgetall("buses")
    if redis_buses:
        for bus_id, data in redis_buses.items():
            bus_data = json.loads(data)
            bus_data["id"] = int(bus_id)
            buses.append(bus_data)
    else:
        buses = db.query(Bus).all()
    return buses

# PATCH /bus/{bus_id}/location → Update bus location
@router.patch("/bus/{bus_id}/location", response_model=BusResponse)
def update_bus_location(bus_id: int, location: BusLocationUpdate, db: Session = Depends(get_db)):
    bus = db.query(Bus).filter(Bus.id == bus_id).first()
    if not bus:
        raise HTTPException(status_code=404, detail="Bus not found")

    bus.latitude = location.latitude
    bus.longitude = location.longitude
    db.commit()
    db.refresh(bus)

    redis_client.hset("buses", bus.id, json.dumps({
        "bus_number": bus.bus_number,
        "latitude": bus.latitude,
        "longitude": bus.longitude
    }))
    return bus
