import logging
from contextlib import asynccontextmanager

from sqlalchemy import NullPool, AsyncAdaptedQueuePool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from src.config import settings

env_db_configs = {
    "test": {
        "url": settings.db_url,
        "echo": settings.echo_sql,
        "poolclass": NullPool,
    },
    "dev": {
        "url": settings.db_url,
        "echo": settings.echo_sql,
        "poolclass": AsyncAdaptedQueuePool,
        "pool_size": 5,
        "max_overflow": 10,
    },
    "prod": {
        "url": settings.db_url,
        "echo": settings.echo_sql,
        "poolclass": AsyncAdaptedQueuePool,
        "pool_size": 20,
        "max_overflow": 40,
        "pool_timeout": 30,
        "pool_recycle": 1800,
    }
}

db_config = env_db_configs.get(settings.environment) or env_db_configs["dev"]

engine = create_async_engine(**db_config)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
Base = declarative_base()

logger = logging.getLogger(__name__)


class DBTransaction:
    async def __aenter__(self):
        self.session = async_session_maker()
        return self.session

    async def __aexit__(self, exc_type, exc_value, traceback):
        try:
            if exc_type is None:
                await self.session.commit()
            else:
                logger.error(
                    "db_error: %s \n Value = %s \n traceback = %s \n",
                    exc_type, exc_value, traceback,
                )
                await self.session.rollback()
        finally:
            await self.session.close()


@asynccontextmanager
async def get_db():
    async with DBTransaction() as session:
        yield session
