from database.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(Base):
    __tablename__ = "users"
    login = Column(String, unique=True, index=True, primary_key=True)
    username = Column(String)
    token = Column(UUID(as_uuid=True), default=uuid.uuid4)