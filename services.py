from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User

async def get_user_by_id(user_id: int, db: AsyncSession ) -> User | None:
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    return user

