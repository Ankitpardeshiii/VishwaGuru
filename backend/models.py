import json
from sqlalchemy import Column, Integer, String, DateTime, Float, Text
from sqlalchemy.types import TypeDecorator
from backend.database import Base

import datetime

class JSONEncodedDict(TypeDecorator):
    """Represents an immutable structure as a json-encoded string."""
    impl = Text
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value

class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    category = Column(String, index=True)
    image_path = Column(String)
    source = Column(String)  # 'telegram', 'web', etc.
    status = Column(String, default="open", index=True)
    created_at = Column(DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc), index=True)
    user_email = Column(String, nullable=True)
    upvotes = Column(Integer, default=0, index=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    location = Column(String, nullable=True)
    action_plan = Column(JSONEncodedDict, nullable=True)
