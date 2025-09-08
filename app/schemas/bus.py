from pydantic import BaseModel

class BusBase(BaseModel):
    number_plate: str
    capacity: int | None = None
    route: str | None = None

class BusCreate(BusBase):
    pass

class BusLocationUpdate(BaseModel):
    latitude: float
    longitude: float

class Bus(BusBase):
    id: int
    latitude: float | None = None
    longitude: float | None = None

    class Config:
        from_attributes = True  # Pydantic v2
