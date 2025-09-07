from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/tickets", tags=["Tickets"])

@router.post("/", response_model=schemas.ticket.Ticket)
def create_ticket(ticket: schemas.ticket.TicketCreate, db: Session = Depends(get_db)):
    return crud.create_ticket(db, ticket)

@router.get("/", response_model=list[schemas.ticket.Ticket])
def get_tickets(db: Session = Depends(get_db)):
    return crud.get_tickets(db)

@router.get("/{ticket_id}", response_model=schemas.ticket.Ticket)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = crud.get_ticket(db, ticket_id)
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket

@router.put("/{ticket_id}", response_model=schemas.ticket.Ticket)
def update_ticket(ticket_id: int, ticket: schemas.ticket.TicketCreate, db: Session = Depends(get_db)):
    db_ticket = crud.update_ticket(db, ticket_id, ticket)
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket

@router.delete("/{ticket_id}")
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    success = crud.delete_ticket(db, ticket_id)
    if not success:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"message": "Ticket deleted successfully"}
