from fastapi import HTTPException
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database.models.purchase import Purchase
from database.schemas.purchase import PurchaseRead, PurchaseCreate

class PurchaseCrud:
    @staticmethod
    async def check_existing(db: AsyncSession, user_id: UUID, link: str) -> bool:
        query = select(Purchase).where((Purchase.user_id == user_id) & (Purchase.link == link))

        result = await db.execute(query)
        existing_purchase = result.scalars().first()

        return existing_purchase is not None
    
    @staticmethod
    async def add_purchase(db: AsyncSession, purchase_data: PurchaseCreate) -> PurchaseRead:
        is_exists = await PurchaseCrud.check_existing(db, purchase_data.user_id, purchase_data.link)
        if is_exists:
            raise HTTPException(status_code=409, detail="Purchase already exists")
        
        new_purchase = Purchase(
            name=purchase_data.name,
            price=purchase_data.price,
            link=purchase_data.link,
            user_id=purchase_data.user_id,
        )
        db.add(new_purchase)

        await db.commit()
        await db.refresh(new_purchase)
        return PurchaseRead.model_validate(new_purchase)