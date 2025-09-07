from pydantic import BaseModel

class BusCreate(BaseModel):
    bus_number: str
    latitude: float
    longitude: float

class BusResponse(BusCreate):   # 👈 Make sure this exists
    id: int

class BusLocationUpdate(BaseModel):
    latitude: float
    longitude: float
