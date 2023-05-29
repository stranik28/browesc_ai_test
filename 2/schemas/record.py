from pydantic import BaseModel

class Record(BaseModel):
    uuid: str
    user: str
    path: str