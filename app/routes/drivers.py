from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/drivers", tags=["Drivers"])

@router.post("/", response_model=schemas.driver.Driver)
def create_driver(driver: schemas.driver.DriverCreate, db: Session = Depends(get_db)):
    return crud.create_driver(db, driver)

@router.get("/", response_model=list[schemas.driver.Driver])
def get_drivers(db: Session = Depends(get_db)):
    return crud.get_drivers(db)

@router.get("/{driver_id}", response_model=schemas.driver.Driver)
def get_driver(driver_id: int, db: Session = Depends(get_db)):
    db_driver = crud.get_driver(db, driver_id)
    if not db_driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return db_driver

@router.put("/{driver_id}", response_model=schemas.driver.Driver)
def update_driver(driver_id: int, driver: schemas.driver.DriverCreate, db: Session = Depends(get_db)):
    db_driver = crud.update_driver(db, driver_id, driver)
    if not db_driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return db_driver

@router.delete("/{driver_id}")
def delete_driver(driver_id: int, db: Session = Depends(get_db)):
    success = crud.delete_driver(db, driver_id)
    if not success:
        raise HTTPException(status_code=404, detail="Driver not found")
    return {"message": "Driver deleted successfully"}
