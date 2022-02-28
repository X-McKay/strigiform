"""Module for Configuring settings."""
import os
import sys
from os.path import dirname
from os.path import join
from strigiform.util import logger
from typing import Optional

import yaml
from dotenv import load_dotenv

logger = logger.logger(name=__name__)

load_dotenv()

_profile_configpath = join(sys.exec_prefix, ".strigiform", "profiles.yaml")
_default_profile_configpath = join(
    dirname(dirname(dirname(os.path.realpath(__file__)))), "profiles.yaml"
)
_default_profile = "default"


def get_configpath() -> str:
    """Return config path."""
    for path in [_profile_configpath]:
        if os.path.exists(path):
            logger.info(f"Loading config from {path}")
            return path

    logger.info(f"Loading config from {_default_profile_configpath}")
    return _default_profile_configpath


def get_config() -> dict:
    """Return config."""
    with open(get_configpath(), "rt") as f:
        return yaml.safe_load(f, Loader=yaml.FullLoader)


class _Config:
    """Configuration class."""

    def __init__(self, profile=Optional[str]):
        """Initialize configuration."""
        profile = (
            os.environ.get("profile")
            if os.environ.get("profile") is not None
            else _default_profile
        )
        """This method is defined to remind you that this is not a static class"""
        self.profile = profile
        self.settings = get_config()[self.profile]

    def rdbms(self):
        """Return RDBMS settings."""
        rdbms_config_path = get_config()[self.profile]["rdbms_config"]
        rdbms_profile = get_config()[self.profile]["rdbms_profile"]

        with open(rdbms_config_path, "rt") as f:
            return yaml.safe_load(f, Loader=yaml.FullLoader)[rdbms_profile]


CONFIG = _Config()
