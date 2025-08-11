from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router

from keyboards.reply import menu_kb

from database.crud.user import UserCrud
from database.schemas.user import UserCreate
from database.core.database import get_db

from messages import GREETINGS, NOT_USERNAME

router = Router()
user_crud = UserCrud()

@router.message(CommandStart())
async def greeting(message: Message):
    username = message.from_user.username
    if username is None:
        await message.answer(NOT_USERNAME)
        return
    
    sticker_id = "CAACAgIAAxkBAAEPB9toh4g6h5H3AAFkWPF8NERoLOsx4K8AAgEBAAJWnb0KIr6fDrjC5jQ2BA"
    
    await message.answer_sticker(sticker=sticker_id)
    await message.answer(GREETINGS, parse_mode="Markdown", reply_markup=menu_kb)

    user_data = {
        "telegram_id": int(message.from_user.id),
        "username": username
    }

    user_data_obj = UserCreate(**user_data)
    
    async for db in get_db():
        new_user = await user_crud.add_user(db=db, user_data=user_data_obj)
        if new_user is None:
            pass
