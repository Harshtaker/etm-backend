from pydantic import BaseModel

class FeedbackBase(BaseModel):
    user_id: int
    bus_id: int
    comment: str

class FeedbackCreate(FeedbackBase):
    pass

class Feedback(FeedbackBase):
    id: int

    class Config:
        orm_mode = True
