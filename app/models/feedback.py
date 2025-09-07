from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    bus_id = Column(Integer, ForeignKey("buses.id"), nullable=True)
    message = Column(String, nullable=False)
    status = Column(String, default="pending")

    user = relationship("User", back_populates="feedbacks")
    bus = relationship("Bus", back_populates="feedbacks")
