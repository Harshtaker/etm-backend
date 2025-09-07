from pydantic import BaseModel, ConfigDict
from datetime import datetime

class TicketBase(BaseModel):
    user_id: int
    bus_id: int
    seat_number: int
    journey_date: datetime

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
