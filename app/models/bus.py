from sqlalchemy import Column, Integer, String
from app.models import Base

class Bus(Base):
    __tablename__ = "buses"
    __table_args__ = {"extend_existing": True}  # add this

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
