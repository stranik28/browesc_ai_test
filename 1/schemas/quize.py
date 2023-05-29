from pydantic import BaseModel
from datetime import datetime , timezone
from pydantic import validator

class Quize(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime
    class Config:
        orm_mode = True

    @validator('created_at')
    def add_timezone(cls, value):
        return value.replace(tzinfo=timezone.utc)