from sqlalchemy.ext.asyncio import create_async_engine
# from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.config import settings

engine = create_async_engine(
    str(settings.SQLALCHEMY_DATABASE_URI),
    echo= (settings.ENVIRONMENT != 'production')
)


async def init_db(session: AsyncSession) -> None:
    pass
