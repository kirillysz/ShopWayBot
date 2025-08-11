from fastapi import HTTPException

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
    async def add_user(db: AsyncSession, user_data: UserCreate) -> UserRead:
        telegram_id = user_data.telegram_id
        if telegram_id is None:
            raise HTTPException(status_code=400, detail="telegram_id is required")

        is_exists = await UserCrud.check_existing(db, telegram_id)
        if is_exists:
            raise HTTPException(status_code=409, detail="User already exists")

        user = User(
            telegram_id=telegram_id,
            username=user_data.username,
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)

        return UserRead.model_validate(user)
    