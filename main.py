from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import (
    AsyncSessionLocal,
    Base,
    engine,
)
from schemas import UserCreate, UserResponse, UserUpdate
from services import get_all_users, get_user_by_id, create_user as service_user_create, update_user as service_update_user, delete_user as service_delete_user


app = FastAPI(title="FastAPI Learning")

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


@app.on_event("startup")
async def on_startup() -> None:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


@app.post("/users", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = await service_user_create(db, user.name)
    return new_user


@app.get("/users", response_model=list[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):
    users = await get_all_users(db)
    return users

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
    
@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_update: UserUpdate, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = await service_update_user(db, user, user_update.name, user_update.hobbies)
    return updated_user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    await service_delete_user(db, user)
    return {"message": f"User with id {user_id} deleted successfully"}