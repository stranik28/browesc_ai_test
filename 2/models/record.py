from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Record(Base):
    __tablename__ = "records"
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    user = Column(String, ForeignKey("users.login"))