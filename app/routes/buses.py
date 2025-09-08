from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.bus import Bus as BusModel
from app.schemas.bus import BusCreate, Bus, BusLocationUpdate

router = APIRouter(prefix="/buses", tags=["buses"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST → create bus
@router.post("/", response_model=Bus)
def create_bus(bus: BusCreate, db: Session = Depends(get_db)):
    db_bus = BusModel(**bus.dict())
    db.add(db_bus)
    db.commit()
    db.refresh(db_bus)
    return db_bus

# PATCH → update location
@router.patch("/{bus_id}/location", response_model=Bus)
def update_bus_location(bus_id: int, location: BusLocationUpdate, db: Session = Depends(get_db)):
    bus = db.query(BusModel).filter(BusModel.id == bus_id).first()
    if not bus:
        raise HTTPException(status_code=404, detail="Bus not found")
    bus.latitude = location.latitude
    bus.longitude = location.longitude
    db.commit()
    db.refresh(bus)
    return bus

# GET → all buses
@router.get("/", response_model=list[Bus])
def get_buses(db: Session = Depends(get_db)):
    return db.query(BusModel).all()
