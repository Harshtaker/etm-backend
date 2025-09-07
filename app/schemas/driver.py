from pydantic import BaseModel, ConfigDict

class DriverBase(BaseModel):
    name: str
    license_number: str

class DriverCreate(DriverBase):
    pass

class Driver(DriverBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
