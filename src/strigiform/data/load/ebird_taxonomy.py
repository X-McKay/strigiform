"""Populate database tables."""
from io import StringIO

import pandas as pd
from pandas.core.frame import DataFrame
from sqlalchemy import create_engine

from strigiform.data.fetch import ebird
from strigiform.util import config
from strigiform.util import logger

logger = logger.logger_init(name=__name__)


def fetch_and_clean_data() -> DataFrame:
    """Fetch latest eBird taxonomy and export to a pandas DataFrame."""
    logger.info("Using eBird API to fetch taxonomy...")
    data = ebird.get_taxonomy()
    logger.info("Data successfully fetched. Performing quick format and tidy...")

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

    return df


if __name__ == "__main__":
    engine = create_engine(config.db_engine_str())  # TODO: Generalize

    df = fetch_and_clean_data()

    logger.info("Loading taxonomy data to db...")
    df.to_sql("taxonomy", engine, if_exists="replace")  # TODO: modify to append delta
    logger.info("Load of eBird taxonomy complete!")
