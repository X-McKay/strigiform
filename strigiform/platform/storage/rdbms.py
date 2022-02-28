"""Setting up PostGres to store data."""
from strigiform.platform.storage.postgresql import Postgresql
from strigiform.settings.provider import Provider
from strigiform.util import logger

logger = logger.logger(name=__name__)


# Hacky - need to fix
PROVIDERS = [Postgresql]
ENGINE = Provider().load_provider_settings("rdbms")["engine"]
TYPE = [provider for provider in PROVIDERS if provider.SQL_ENGINE_TYPE == ENGINE][0]


class RDBMSProvider(Provider):
    """Generic RDBMS provider."""

    PROVIDERS = [Postgresql]
    LOOKUP = {provider.SQL_ENGINE_TYPE: provider for provider in PROVIDERS}

    def __init__(self, type: str = TYPE):
        """Abstract RDBMS provider."""
        logger.info(f"Engine set to {type}")

        self.provider = None

        # if type not in self.LOOKUP:
        #     providers = ", ".join(self.LOOKUP.keys())
        #     raise Exception(
        #         f"{type} Engine not found. Available engines are: {providers}"
        #     )

        self.provider = type()

        logger.info(f"RDBMS Provider set to {self.provider}")

    def __getattr__(self, attr: str):
        """Return attribute from provider."""
        return getattr(self.provider, attr)
