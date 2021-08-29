"""File to store ibyrd configurations."""
# eBird API 2.0: https://documenter.getpostman.com/view/664302/S1ENwy59#intro
# eBird 2.0 URLS
EBIRD_HOTSPOT_URL = "https://api.ebird.org/v2/ref/hotspot/geo?"
EBIRD_TAXONOMY_URL = "https://ebird.org/ws2.0/ref/taxonomy/ebird"

# Default values related to Hotspot requests
DEFAULT_LAT = 40.71
DEFAULT_LON = -73.95
DEFAULT_FORMAT = "json"
DEFAULT_DIST = 3
DEFAULT_BACK = 5

# Default values related to Taxonomy requests
DEFAULT_TAXONOMY_FORMAT = "csv"
DEFAULT_TAXONOMY_CATEGORY = "Species"

# Default values related to Checklist requests
DEFAULT_LOCALE = "en"
DEFAULT_DETAIL = "simple"
DEFAULT_HOTSPOTS_ONLY = "false"
DEFAULT_PROVISIONAL = "false"
DEFAULT_RANK = "mrec"
DEFAULT_MAX_OBSERVATIONS = None
DEFAULT_MAX_LOCATIONS = 10
