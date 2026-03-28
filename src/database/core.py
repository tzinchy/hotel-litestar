from datetime import datetime, timezone

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedColumn

from src.config import settings


class Base(DeclarativeBase):
    created_at: Mapped[datetime] = MappedColumn(default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = MappedColumn(default=datetime.now(timezone.utc))


engine = create_async_engine(
    str(settings.DB),
    pool_size=5,
    max_overflow=0,
    echo=False,
)

Session = async_sessionmaker(engine, expire_on_commit=False)
