from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import AsyncSessionLocal
from models import User
from schemas import UserCreate, UserResponse


app = FastAPI(title="FastAPI Learning")

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

