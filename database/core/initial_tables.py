from database.core.database import engine, Base

from database.models.user import User
from database.models.purchase import Purchase

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)