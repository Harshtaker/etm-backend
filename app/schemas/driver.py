from pydantic import BaseModel

class DriverBase(BaseModel):
    name: str
    license_number: str
    phone: str | None = None

class DriverCreate(DriverBase):
    pass

class Driver(DriverBase):
    id: int

    class Config:
        orm_mode = True
