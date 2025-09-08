from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.database import Base

class BusStop(Base):
    __tablename__ = "bus_stops"

    id = Column(Integer, primary_key=True, index=True)
    bus_id = Column(Integer, ForeignKey("buses.id"), nullable=False)
    name = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    stop_order = Column(Integer, nullable=False)  # order in the route
