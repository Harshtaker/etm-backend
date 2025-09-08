from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.bus_stop import BusStop as BusStopModel
from app.schemas.bus_stop import BusStopCreate, BusStop

router = APIRouter(prefix="/bus_stops", tags=["bus_stops"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST /bus_stops/ → Add a bus stop
@router.post("/", response_model=BusStop)
def create_bus_stop(stop: BusStopCreate, db: Session = Depends(get_db)):
    db_stop = BusStopModel(**stop.dict())
    db.add(db_stop)
    db.commit()
    db.refresh(db_stop)
    return db_stop

# GET /bus_stops/{bus_id} → Get all stops of a bus
@router.get("/{bus_id}", response_model=list[BusStop])
def get_bus_stops(bus_id: int, db: Session = Depends(get_db)):
    return db.query(BusStopModel).filter(BusStopModel.bus_id == bus_id).order_by(BusStopModel.stop_order).all()
