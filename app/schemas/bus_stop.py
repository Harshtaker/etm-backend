from pydantic import BaseModel

class BusStopBase(BaseModel):
    bus_id: int
    name: str
    latitude: float
    longitude: float
    stop_order: int

class BusStopCreate(BusStopBase):
    pass

class BusStop(BusStopBase):
    id: int

    class Config:
        from_attributes = True
