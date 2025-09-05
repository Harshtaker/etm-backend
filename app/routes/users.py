from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserRead
from app.models.user import User
from app.services import get_db

router = APIRouter(prefix="/users", tags=["users"])

# Create user
@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get all users
@router.get("/", response_model=list[UserRead])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
