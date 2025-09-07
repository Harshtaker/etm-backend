from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    bus_id = Column(Integer, ForeignKey("buses.id"))
    seat_number = Column(String, nullable=False)
    status = Column(String, default="booked")

    # Relationships
    user = relationship("User", back_populates="tickets")
    bus = relationship("Bus", back_populates="tickets")
