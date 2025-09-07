from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/feedbacks", tags=["Feedbacks"])

@router.post("/", response_model=schemas.feedback.Feedback)
def create_feedback(feedback: schemas.feedback.FeedbackCreate, db: Session = Depends(get_db)):
    return crud.create_feedback(db, feedback)

@router.get("/", response_model=list[schemas.feedback.Feedback])
def get_feedbacks(db: Session = Depends(get_db)):
    return crud.get_feedbacks(db)

@router.get("/{feedback_id}", response_model=schemas.feedback.Feedback)
def get_feedback(feedback_id: int, db: Session = Depends(get_db)):
    db_feedback = crud.get_feedback(db, feedback_id)
    if not db_feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return db_feedback

@router.put("/{feedback_id}", response_model=schemas.feedback.Feedback)
def update_feedback(feedback_id: int, feedback: schemas.feedback.FeedbackCreate, db: Session = Depends(get_db)):
    db_feedback = crud.update_feedback(db, feedback_id, feedback)
    if not db_feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return db_feedback

@router.delete("/{feedback_id}")
def delete_feedback(feedback_id: int, db: Session = Depends(get_db)):
    success = crud.delete_feedback(db, feedback_id)
    if not success:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return {"message": "Feedback deleted successfully"}
