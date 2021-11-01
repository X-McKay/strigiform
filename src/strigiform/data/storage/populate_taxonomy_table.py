"""Populate database tables."""
from io import StringIO

import pandas as pd
from sqlalchemy import create_engine

from strigiform.data.fetch import ebird
from strigiform.util import config

data = ebird.get_taxonomy()
temp_data = StringIO(data, newline="\n")
df = pd.read_csv(temp_data)

df.columns = [
    "scientific_name",
    "common_name",
    "species_code",
    "category",
    "taxon_order",
    "com_name_codes",
    "sci_name_codes",
    "banding_codes",
    "order_name",
    "family_com_name",
    "family_sci_name",
    "report_as",
    "extinct",
    "extinct_year",
    "family_code",
]

# read the connection parameters
# params = config.postgres_config() # TODO: Generalize with specific config as param
# connect to the PostgreSQL server
# conn = psycopg2.connect(**params)

engine = create_engine(config.db_engine_str())  # TODO: Generalize

df.to_sql("taxonomy", engine, if_exists="replace")  # TODO: modify to append delta
