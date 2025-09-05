from pydantic import BaseModel
from pydantic import ConfigDict

class BusCreate(BaseModel):
    bus_number: str
    latitude: float
    longitude: float

class BusResponse(BusCreate):
    id: int

model_config = ConfigDict(from_attributes=True)


class BusLocationUpdate(BaseModel):
    latitude: float
    longitude: float

