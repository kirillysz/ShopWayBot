from aiogram.fsm.state import State, StatesGroup

class ItemState(StatesGroup):
    name = State()
    link = State()