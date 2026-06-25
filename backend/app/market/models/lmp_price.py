from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.base import Base

class LMPPrice(Base):

    __tablename__ = "lmp_prices"

    ts: Mapped[str] = mapped_column(
        TIMESTAMP,
        primary_key=True
    )

    node: Mapped[str] = mapped_column(
        String,
        primary_key=True
    )

    market: Mapped[str] = mapped_column(
        String,
        primary_key=True
    )

    lmp: Mapped[float] = mapped_column(
        Float
    )