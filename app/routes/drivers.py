from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database, models, schemas

router = APIRouter(prefix="/drivers", tags=["drivers"])

@router.post("/", response_model=schemas.driver.Driver)
def create_driver(driver: schemas.driver.DriverCreate, db: Session = Depends(database.get_db)):
    new_driver = models.driver.Driver(**driver.dict())
    db.add(new_driver)
    db.commit()
    db.refresh(new_driver)
    return new_driver

@router.get("/", response_model=list[schemas.driver.Driver])
def get_drivers(db: Session = Depends(database.get_db)):
    return db.query(models.driver.Driver).all()

@router.get("/{driver_id}", response_model=schemas.driver.Driver)
def get_driver(driver_id: int, db: Session = Depends(database.get_db)):
    return db.query(models.driver.Driver).filter(models.driver.Driver.id == driver_id).first()
