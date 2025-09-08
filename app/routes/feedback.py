from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database, models, schemas

router = APIRouter(prefix="/feedback", tags=["feedback"])

@router.post("/", response_model=schemas.feedback.Feedback)
def create_feedback(feedback: schemas.feedback.FeedbackCreate, db: Session = Depends(database.get_db)):
    new_feedback = models.feedback.Feedback(**feedback.dict())
    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)
    return new_feedback

@router.get("/", response_model=list[schemas.feedback.Feedback])
def get_feedbacks(db: Session = Depends(database.get_db)):
    return db.query(models.feedback.Feedback).all()
