from dotenv import load_dotenv
from os import getenv

load_dotenv(dotenv_path=".env")

class Config:
    BOT_TOKEN: str = getenv("BOT_TOKEN")
    DATABASE_URL: str = getenv("DATABASE_URL")
    EXCHANGE_TOKEN: str = getenv("EXCHANGE_TOKEN")
    MANAGER_IDS: int = getenv("MANAGER_IDS")

config = Config()