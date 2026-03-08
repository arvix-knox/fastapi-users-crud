from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User


async def get_user_by_id(db: AsyncSession, user_id: int) -> User | None:
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def get_all_users(db: AsyncSession) -> list[User]:
    result = await db.execute(select(User))
    return result.scalars().all()


async def create_user(db: AsyncSession, name: str) -> User:
    new_user = User(name=name, hobbies=["reading"])
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def update_user(db: AsyncSession, user: User, name: str, hobbies: list[str]) -> User:
    user.name = name
    user.hobbies = hobbies
    await db.commit()
    await db.refresh(user)
    return user


async def delete_user(db: AsyncSession, user: User) -> None:
    await db.delete(user)
    await db.commit()