from fastapi import HTTPException
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database.models.purchase import Purchase
from database.schemas.purchase import PurchaseRead, PurchaseCreate

class PurchaseCrud:
    @staticmethod
    async def check_existing(db: AsyncSession, user_id: int, link: str) -> bool:
        result = await db.execute(
            select(Purchase)
            .where(Purchase.telegram_id == user_id)
            .where(Purchase.link == link)
        )
        return result.scalars().first() is not None
    
    @staticmethod
    async def add_purchase(db: AsyncSession, purchase_data: dict) -> PurchaseRead:
        is_exists = await PurchaseCrud.check_existing(db, purchase_data.telegram_id, purchase_data.link)
        if is_exists:
            raise HTTPException(status_code=409, detail="Purchase already exists")
        
        new_purchase = Purchase(
            item_name=purchase_data.item_name,
            link=purchase_data.link,
            telegram_id=purchase_data.telegram_id,
        )
        db.add(new_purchase)

        await db.commit()
        await db.refresh(new_purchase)
        
        return PurchaseRead.model_validate(new_purchase)
        