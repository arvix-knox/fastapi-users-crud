from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import (
    AsyncSessionLocal,
    Base,
    engine,
)
from models import User
from schemas import UserCreate, UserResponse, UserUpdate


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
    new_user = User(name=user.name, hobbies=["reading"])
    try:
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
    except SQLAlchemyError as exc:
        await db.rollback()
        raise HTTPException(status_code=500, detail="Database write error") from exc

    return new_user


@app.get("/users", response_model=list[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(User))
        return result.scalars().all()
    except SQLAlchemyError as exc:
        raise HTTPException(status_code=500, detail="Database read error") from exc


@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    if user is  None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
    
@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_update: UserUpdate, db: AsyncSession = Depends(get_db)):
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    if user is  None:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = user_update.name
    user.hobbies = user_update.hobbies
    await db.commit()
    await db.refresh(user)
    return user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    if user is  None:
        raise HTTPException(status_code=404, detail="User not found")
    await db.delete(user)
    await db.commit()
    return {"message": f"User with id {user_id} deleted successfully"}