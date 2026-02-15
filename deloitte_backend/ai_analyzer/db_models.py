from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

# --- FIX: ABSOLUTE IMPORT ---
# Now that we added PYTHONPATH=. to the .env file, this will work perfectly.
from services.database import Base 

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    test_runs = relationship("TestRun", back_populates="owner")

class TestRun(Base):
    __tablename__ = "test_runs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    project_path = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    json_data = Column(Text) 
    
    owner = relationship("User", back_populates="test_runs")