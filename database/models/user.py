from typing import List, Optional
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy import String, BigInteger

from database.core.database import Base
from database.models.purchase import Purchase

class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True)

    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[Optional[str]] = mapped_column(String, nullable=False)

    purchases: Mapped[List[Purchase]] = relationship(
        "Purchase", back_populates="user", cascade="all, delete-orphan"
    )
