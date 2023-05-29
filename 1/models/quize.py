from sqlalchemy import Column, Integer, String, DateTime
from database.database import Base

class Quize(Base):
    __tablename__ = "quize"
    id = Column(Integer, primary_key=True)
    question = Column(String(1024))
    answer = Column(String(1024))
    created_at = Column(DateTime(timezone=True))