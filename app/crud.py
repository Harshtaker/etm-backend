from sqlalchemy.orm import Session
from app import models, schemas

# ---------------- USERS ----------------
def create_user(db: Session, user: schemas.user.UserCreate):
    db_user = models.user.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.user.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.user.User).filter(models.user.User.id == user_id).first()

def update_user(db: Session, user_id: int, user: schemas.user.UserCreate):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if not db_user:
        return False
    db.delete(db_user)
    db.commit()
    return True


# ---------------- BUSES ----------------
def create_bus(db: Session, bus: schemas.bus.BusCreate):
    db_bus = models.bus.Bus(**bus.dict())
    db.add(db_bus)
    db.commit()
    db.refresh(db_bus)
    return db_bus

def get_buses(db: Session):
    return db.query(models.bus.Bus).all()

def get_bus(db: Session, bus_id: int):
    return db.query(models.bus.Bus).filter(models.bus.Bus.id == bus_id).first()

def update_bus(db: Session, bus_id: int, bus: schemas.bus.BusCreate):
    db_bus = get_bus(db, bus_id)
    if not db_bus:
        return None
    for key, value in bus.dict().items():
        setattr(db_bus, key, value)
    db.commit()
    db.refresh(db_bus)
    return db_bus

def delete_bus(db: Session, bus_id: int):
    db_bus = get_bus(db, bus_id)
    if not db_bus:
        return False
    db.delete(db_bus)
    db.commit()
    return True


# ---------------- DRIVERS ----------------
def create_driver(db: Session, driver: schemas.driver.DriverCreate):
    db_driver = models.driver.Driver(**driver.dict())
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver

def get_drivers(db: Session):
    return db.query(models.driver.Driver).all()

def get_driver(db: Session, driver_id: int):
    return db.query(models.driver.Driver).filter(models.driver.Driver.id == driver_id).first()

def update_driver(db: Session, driver_id: int, driver: schemas.driver.DriverCreate):
    db_driver = get_driver(db, driver_id)
    if not db_driver:
        return None
    for key, value in driver.dict().items():
        setattr(db_driver, key, value)
    db.commit()
    db.refresh(db_driver)
    return db_driver

def delete_driver(db: Session, driver_id: int):
    db_driver = get_driver(db, driver_id)
    if not db_driver:
        return False
    db.delete(db_driver)
    db.commit()
    return True


# ---------------- TICKETS ----------------
def create_ticket(db: Session, ticket: schemas.ticket.TicketCreate):
    db_ticket = models.ticket.Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def get_tickets(db: Session):
    return db.query(models.ticket.Ticket).all()

def get_ticket(db: Session, ticket_id: int):
    return db.query(models.ticket.Ticket).filter(models.ticket.Ticket.id == ticket_id).first()

def update_ticket(db: Session, ticket_id: int, ticket: schemas.ticket.TicketCreate):
    db_ticket = get_ticket(db, ticket_id)
    if not db_ticket:
        return None
    for key, value in ticket.dict().items():
        setattr(db_ticket, key, value)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def delete_ticket(db: Session, ticket_id: int):
    db_ticket = get_ticket(db, ticket_id)
    if not db_ticket:
        return False
    db.delete(db_ticket)
    db.commit()
    return True


# ---------------- FEEDBACKS ----------------
def create_feedback(db: Session, feedback: schemas.feedback.FeedbackCreate):
    db_feedback = models.feedback.Feedback(**feedback.dict())
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

def get_feedbacks(db: Session):
    return db.query(models.feedback.Feedback).all()

def get_feedback(db: Session, feedback_id: int):
    return db.query(models.feedback.Feedback).filter(models.feedback.Feedback.id == feedback_id).first()

def update_feedback(db: Session, feedback_id: int, feedback: schemas.feedback.FeedbackCreate):
    db_feedback = get_feedback(db, feedback_id)
    if not db_feedback:
        return None
    for key, value in feedback.dict().items():
        setattr(db_feedback, key, value)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

def delete_feedback(db: Session, feedback_id: int):
    db_feedback = get_feedback(db, feedback_id)
    if not db_feedback:
        return False
    db.delete(db_feedback)
    db.commit()
    return True
