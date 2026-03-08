from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from database import AsyncSession
from models import User
from schemas import UserCreate, UserUpdate



async def get_user_by_id(db: AsyncSession, user_id: int ) -> User | None:
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    return user

async def get_all_users(db: AsyncSession, users: int) -> list[User]:
    query = select(User)
    result = await db.execute(query)
    users = result.scalars().all()
    return users

async def create_user(user: UserCreate, db: AsyncSession):
    new_user = User(name=user.name, hobbies=["reading"])
    try:
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
    except SQLAlchemyError as exc:
        await db.rollback()
        raise ModuleNotFoundError(status_code=500, detail="Database write error") from exc

    return new_user

async def update_user(user_id: int, user_update: UserUpdate, db: AsyncSession ):
    user = get_user_by_id()
    if user is None:
        raise ModuleNotFoundError(status_code=404, detail="User not found")
    user.name = user_update.name
    user.hobbies = user_update.hobbies
    await db.commit()
    await db.refresh(user)
    return user

async def delete_user(user_id: int, db: AsyncSession):
    user = get_user_by_id()
    if user is None:
        raise ModuleNotFoundError(status_code=404, detail="User not found")
    await db.delete(user)
    await db.commit()
    return {"message": f"User with id {user_id} deleted successfully"}


