from pydantic import BaseModel
from datetime import datetime

class BusTrackingBase(BaseModel):
    bus_id: int
    latitude: float
    longitude: float

class BusTrackingCreate(BusTrackingBase):
    pass

class BusTracking(BusTrackingBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True
