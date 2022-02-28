"""Add data sources to Grafana."""
import json
import os
from strigiform.settings.provider import Provider
from strigiform.util import logger

import requests

logger = logger.logger(name=__name__)

grafana = Provider().load_provider_settings("grafana")
rdbms = Provider().load_provider_settings("rdbms")

grafana_url = os.path.join(
    "http://", "%s:%u" % (grafana["host"], grafana["port"]), "api"
)
session = requests.Session()
login_post = session.post(
    os.path.join(grafana_url, "login"),
    data=json.dumps(
        {
            "user": grafana["user"],
            "email": "admin@localhost",
            "secureJsonData": {"password": grafana["password"]},
        }
    ),
    headers={"content-type": "application/json"},
)

# Get list of datasources
datasources_get = session.get(os.path.join(grafana_url, "api", "datasources"))
datasources = datasources_get.json()

# Add new datasource
datasources_put = session.put(
    os.path.join(grafana_url, "api", "datasources"),
    data=json.dumps(
        {
            "access": "direct",
            "database": rdbms["database"],
            "name": rdbms["engine"],
            "secureJsonData": {"password": rdbms["password"]},
            "type": "postgres",
            "url": "http://%s:%u" % (rdbms["host"], rdbms["port"]),
            "user": rdbms["user"],
        }
    ),
    headers={"content-type": "application/json"},
)
