from aiogram.types import Message
from aiogram import Router
from aiogram import F

from database.crud.user import UserCrud
from database.core.database import get_db


router = Router()
user_crud = UserCrud()

@router.message(F.text == "👤Профиль")
async def get_profile(message: Message):
    async for db in get_db():
        user = await user_crud.get_user(db=db, telegram_id=int(message.from_user.id))
    
    if user is None:
        await message.answer("Пользователь не найден. Зарегистрируйтесь через /start")
        return

    text = (
        f"👤 Ваш профиль:\n"
        f"Telegram ID: {user.telegram_id}\n"
        f"Username: @{user.username}\n"
        f"Покупки: {user.purchases}\n"
    )
    await message.answer(text)


