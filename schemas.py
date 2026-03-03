from pydantic import BaseModel
from typing import Optional
class UserCreate(BaseModel):
    name: str

class UserResponse(BaseModel):
    id: int
    name: str
    hobbies: list[str]
    model_config = {"from_attributes": True}

class UserUpdate(BaseModel):
    name: Optional[str] = None
    hobbies:  Optional[list[str]] = None