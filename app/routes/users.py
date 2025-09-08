from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database, models, schemas

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=schemas.user.User)
def create_user(user: schemas.user.UserCreate, db: Session = Depends(database.get_db)):
    new_user = models.user.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/", response_model=list[schemas.user.User])
def get_users(db: Session = Depends(database.get_db)):
    return db.query(models.user.User).all()
