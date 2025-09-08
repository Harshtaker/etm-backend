from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Bus(Base):
    __tablename__ = "buses"

    id = Column(Integer, primary_key=True, index=True)
    number_plate = Column(String, unique=True, nullable=False)
    capacity = Column(Integer, nullable=True)
    route = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
