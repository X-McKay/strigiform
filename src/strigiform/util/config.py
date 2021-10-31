"""File to store strigiform configurations."""
from configparser import ConfigParser

# TODO: allow AWS, local, etc.
DEFAULT_SECRET_PROVIDER = "vault"  # noqa: S105

# eBird API 2.0: https://documenter.getpostman.com/view/664302/S1ENwy59#intro
# eBird 2.0 URLS
EBIRD_HOTSPOT_URL = "https://api.ebird.org/v2/ref/hotspot/geo?"
EBIRD_TAXONOMY_URL = "https://ebird.org/ws2.0/ref/taxonomy/ebird"

# Default values related to Hotspot requests
DEFAULT_LAT = 40.71
DEFAULT_LNG = -73.95
DEFAULT_FORMAT = "json"
DEFAULT_SAVE_FORMAT = "json"
DEFAULT_DIST = 5
DEFAULT_BACK = 5

# Default values related to Taxonomy requests
DEFAULT_TAXONOMY_FORMAT = "csv"
DEFAULT_TAXONOMY_SAVE_FORMAT = "csv"
DEFAULT_TAXONOMY_CATEGORY = "species"

# Default values related to Checklist requests
DEFAULT_LOCALE = "en"
DEFAULT_DETAIL = "simple"
DEFAULT_HOTSPOTS_ONLY = "false"
DEFAULT_PROVISIONAL = "false"
DEFAULT_RANK = "mrec"
DEFAULT_MAX_OBSERVATIONS = None
DEFAULT_MAX_LOCATIONS = 10


def db_config(filename="database.ini", section="postgresql"):
    """Parse postgres connection info from ini file.

    :param filename: database configuration file, defaults to "database.ini"
    :type filename: str, optional
    :param section: section of configuration file, defaults to "postgresql"
    :type section: str, optional
    :raises Exception: if section is not found in configuration file
    :return: dictionary with connection information
    :rtype: dict
    """
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            "Section {0} not found in the {1} file".format(section, filename)
        )

    return db


def db_engine_str(filename="database.ini", section="postgresql"):
    """Generate connection string from database.ini file.

    :return: connection string for sqlalchemy
    :rtype: string
    """
    config = db_config(filename, section)
    user = config["user"]
    password = config["password"]
    host = config["host"]
    database = config["database"]
    return f"{section}://{user}:{password}@{host}/{database}"
