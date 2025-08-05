from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Transcription(Base):
    __tablename__ = "transcriptions"
    id = Column(Integer, primary_key=True, index=True)
    call_id = Column(String, index=True)
    agent_id = Column(String, index=True)
    customer_id = Column(String, index=True)
    transcript = Column(Text)
    diarization = Column(Text)
    sentiment = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
