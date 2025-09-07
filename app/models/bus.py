from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base  # absolute import

class Bus(Base):
    __tablename__ = "buses"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=True)
    route_id = Column(Integer, ForeignKey("routes.id"), nullable=True)

    tickets = relationship("Ticket", back_populates="bus")
    feedbacks = relationship("Feedback", back_populates="bus")
    driver = relationship("Driver", back_populates="buses")
