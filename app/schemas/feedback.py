from pydantic import BaseModel, ConfigDict

class FeedbackBase(BaseModel):
    user_id: int
    bus_id: int
    rating: int
    comment: str

class FeedbackCreate(FeedbackBase):
    pass

class Feedback(FeedbackBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
