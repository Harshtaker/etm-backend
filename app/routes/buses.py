from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.bus import BusCreate, BusRead
from app.models.bus import Bus
from app.services import get_db

router = APIRouter(prefix="/buses", tags=["buses"])

# Create bus
@router.post("/", response_model=BusRead)
def create_bus(bus: BusCreate, db: Session = Depends(get_db)):
    db_bus = Bus(name=bus.name, capacity=bus.capacity)
    db.add(db_bus)
    db.commit()
    db.refresh(db_bus)
    return db_bus

# Get all buses
@router.get("/", response_model=list[BusRead])
def get_buses(db: Session = Depends(get_db)):
    return db.query(Bus).all()
