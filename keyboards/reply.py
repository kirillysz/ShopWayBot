from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Профиль"), KeyboardButton(text="Заказать")],
        [KeyboardButton(text="Калькулятор")]
    ],
    resize_keyboard=True
)
