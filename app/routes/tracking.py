from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.tracking import BusTracking
from app.schemas.tracking import BusTrackingCreate, BusTracking

router = APIRouter(prefix="/tracking", tags=["tracking"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=BusTracking)
def create_tracking(tracking: BusTrackingCreate, db: Session = Depends(get_db)):
    db_tracking = BusTracking(**tracking.dict())
    db.add(db_tracking)
    db.commit()
    db.refresh(db_tracking)
    return db_tracking

@router.get("/{bus_id}", response_model=list[BusTracking])
def get_tracking(bus_id: int, db: Session = Depends(get_db)):
    return db.query(BusTracking).filter(BusTracking.bus_id == bus_id).all()
