from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database.models.user import User
from database.schemas.user import UserRead, UserCreate

class UserCrud:
    @staticmethod
    async def check_existing(db: AsyncSession, telegram_id: int) -> bool:
        query = select(User).where(User.telegram_id == telegram_id)
        result = await db.execute(query)
        existing_user = result.scalars().first()
        return existing_user is not None
    
    @staticmethod
    async def add_user(db: AsyncSession, user_data: UserCreate) -> UserRead | None:
        telegram_id = getattr(user_data, "telegram_id", None)
        if telegram_id is None:
            return None

        if await UserCrud.check_existing(db, telegram_id):
            return None

        user = User(
            telegram_id=telegram_id,
            username=user_data.username,
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)

        return UserRead.model_validate(user)
    
    @staticmethod
    async def get_user(db: AsyncSession, telegram_id: int) -> UserRead | None:
        query = select(User).where(User.telegram_id == telegram_id)
        result = await db.execute(query)

        user = result.scalars().first()
        if user is None:
            return None
        
        return UserRead.model_validate(user)
