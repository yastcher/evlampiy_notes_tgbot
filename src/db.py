from sqlalchemy import NullPool, AsyncAdaptedQueuePool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from src.config import settings

Base = declarative_base()

env_db_configs = {
    "test": {
        "url": settings.local_auth_db,
        "echo": settings.echo_sql,
        "poolclass": NullPool,
    },
    "dev": {
        "url": settings.local_auth_db,
        "echo": settings.echo_sql,
        "poolclass": AsyncAdaptedQueuePool,
        "pool_size": 5,
        "max_overflow": 10,
    },
}

if settings.environment in env_db_configs:
    db_config = env_db_configs.get(settings.environment)
else:
    db_config = env_db_configs.get("dev")

engine = create_async_engine(**db_config)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
