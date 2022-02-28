"""Data model Taxonomy table."""
from strigiform.data.model import observations  # noqa: F401
from strigiform.data.model import taxonomy  # noqa: F401
from strigiform.platform.storage.rdbms import RDBMSProvider
from strigiform.util import logger

from sqlmodel import SQLModel

# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.asyncio import AsyncSession

logger = logger.logger(name=__name__)

rdbms = RDBMSProvider()


def check_if_db_exists():
    """Validate if project db exists."""
    return rdbms.database in rdbms.list_databases()


def create_tables():
    """Create tables."""
    logger.info("Creating tables in defined in './strigiform/data/model/'")
    engine = rdbms.get_engine()
    SQLModel.metadata.create_all(engine)


# TODO: implement async functionalitiy
# async def init_db():
#     async with self.engine.begin() as conn:
#     # await conn.run_sync(SQLModel.metadata.drop_all)
#         await conn.run_sync(SQLModel.metadata.create_all)


def main():
    """Main initialization of db and tables."""
    # Create database if it does not exist
    if not check_if_db_exists():
        logger.info("Database does not exist. Creating database.")
        rdbms.create_database()
    else:
        logger.info("Database exists. Skipping creation.")

    create_tables()


if __name__ == "__main__":
    """Run main."""
    main()
