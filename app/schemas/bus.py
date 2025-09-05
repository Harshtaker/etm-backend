from pydantic import BaseModel, ConfigDict

class BusCreate(BaseModel):
    name: str
    capacity: int

class BusRead(BusCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)  # Pydantic v2
