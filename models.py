from sqlalchemy import ARRAY, Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    hobbies = Column(ARRAY(String))
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)