from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud
from app.schemas.bus import BusCreate, BusResponse, BusLocationUpdate  # direct import

router = APIRouter(prefix="/buses", tags=["Buses"])

@router.post("/", response_model=BusResponse)
def create_bus(bus: BusCreate, db: Session = Depends(get_db)):
    return crud.create_bus(db, bus)

@router.get("/", response_model=list[BusResponse])
def get_buses(db: Session = Depends(get_db)):
    return crud.get_buses(db)

@router.get("/{bus_id}", response_model=BusResponse)
def get_bus(bus_id: int, db: Session = Depends(get_db)):
    db_bus = crud.get_bus(db, bus_id)
    if not db_bus:
        raise HTTPException(status_code=404, detail="Bus not found")
    return db_bus

@router.put("/{bus_id}", response_model=BusResponse)
def update_bus(bus_id: int, bus: BusCreate, db: Session = Depends(get_db)):
    db_bus = crud.update_bus(db, bus_id, bus)
    if not db_bus:
        raise HTTPException(status_code=404, detail="Bus not found")
    return db_bus

@router.delete("/{bus_id}")
def delete_bus(bus_id: int, db: Session = Depends(get_db)):
    success = crud.delete_bus(db, bus_id)
    if not success:
        raise HTTPException(status_code=404, detail="Bus not found")
    return {"message": "Bus deleted successfully"}
