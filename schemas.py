from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str

class UserResponse(BaseModel):
    id: int
    name: str
    hobbies: list[str]
    model_config = {"from_attributes": True}

    