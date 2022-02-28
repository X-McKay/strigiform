"""Generic provider class."""
from strigiform.settings.config import CONFIG

import yaml


class Provider:
    """Base class for inheriting settings."""

    def __init__(self):
        """Initialize provider."""
        self.config = CONFIG
        self.settings = CONFIG.settings

    def load_provider_settings(self, provider):
        """Loads profile settings."""
        provider_config_path = self.settings[provider]["path"]
        provider_profile = self.settings[provider]["profile"]

        with open(provider_config_path, "rt") as f:
            return yaml.safe_load(f, Loader=yaml.FullLoader)[provider_profile]
