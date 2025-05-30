from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from .database import Base

class Content(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    notion_url = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow) 