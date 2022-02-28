"""Setting up PostGres to store data."""
import os
import urllib
from strigiform.settings.provider import Provider
from strigiform.util import logger

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine


logger = logger.logger(name=__name__)

# Hacky - need to fix
RDBMS_SETTNGS = Provider().load_provider_settings("rdbms")


class Postgresql(Provider):
    """Postgresql specific storage methods."""

    SQL_ENGINE_TYPE = "postgresql"

    def __init__(self):
        """Initialize Postgresql provider."""
        rdbms_settings = RDBMS_SETTNGS
        self.engine = rdbms_settings["engine"]
        self.host = rdbms_settings["host"]
        self.database = rdbms_settings["database"]
        self.port = rdbms_settings["port"]
        self.user = rdbms_settings["user"]
        self.password = rdbms_settings["password"]
        self.ssl_mode = urllib.parse.quote_plus(
            str(os.environ.get("ssl_mode", "prefer"))
        )
        self.gen_connection_str = (
            f"{self.engine}://{self.user}:{self.password}@{self.host}:{self.port}"
        )
        self.connection_str = f"{self.gen_connection_str}/{self.database}"
        self.metadata = MetaData()
        self.set_async = False
        self._create_engine()

    def _get_conn_str(self):
        """Return connection string."""
        return self.connection_str

    # def _get_api_conn_str(self):
    #     """Return API connection string."""
    #     return f"{self.connection_str}?sslmode={self.ssl_mode}"

    def _create_engine(self):
        """Create engine."""
        if self.set_async:
            self.engine = create_async_engine(
                self.connection_str, echo=True, future=True
            )

        # TODO: allow async connections
        else:
            self.engine = create_engine(
                self.connection_str, pool_size=3, max_overflow=0
            )

    # def create_db_instance(self):

    #     self.database = Database(self._get_api_conn_str())
    #     return self.database

    def get_engine(self):
        """Return db engine."""
        return self.engine

    def create_database(self):
        """Create config driven project database."""
        try:
            engine = create_engine(f"{self.gen_connection_str}/postgres")
            conn = engine.connect()
            conn.execute("commit")
            conn.execute(f"CREATE DATABASE {self.database};")
            conn.close()
            logger.info(f"Created database: {self.database}")
        except RuntimeError:
            logger.error(f"Unable to create database: {self.database}")

    def list_databases(self):
        """List databases on postgres server."""
        engine = create_engine(f"{self.gen_connection_str}/postgres")
        db_list = engine.execute("SELECT datname FROM pg_database;").fetchall()
        flat_db_list = [item for sublist in db_list for item in sublist]
        return flat_db_list

    def list_tables(self):
        """List tables on postgres server."""
        metadata = MetaData()
        metadata.reflect(self.engine)
        return metadata.tables.keys()
