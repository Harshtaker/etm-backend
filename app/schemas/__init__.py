from pydantic import BaseModel

class BusCreate(BaseModel):
    bus_number: str
    latitude: float
    longitude: float

class BusResponse(BusCreate):
    id: int

    class Config:
        orm_mode = True

class BusLocationUpdate(BaseModel):
    latitude: float
    longitude: float

