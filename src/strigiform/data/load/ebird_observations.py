"""Populate database tables."""
import argparse

import pandas as pd
from sqlalchemy import create_engine

from strigiform.util import config
from strigiform.util import logger

logger = logger.logger_init(name=__name__)


def read_and_clean_data(file_path):
    """Read eBird csv export to a pandas DataFrame.

    :param args: file path
    :type args: string
    :return: Ebird extract of personal submissions
    :rtype: pandas DataFrame
    """
    logger.info("Reading eBird observation export from {file_path}")
    df = pd.read_csv(file_path)
    logger.info("Data successfully read. Performing quick tidy up.")

    df.columns = [
        "submission_id",
        "common_name",
        "scientific_name",
        "taxon_order",
        "count",
        "state",
        "county",
        "location_id",
        "location",
        "lat",
        "lng",
        "date",
        "time",
        "protocol",
        "duration_min",
        "all_obs_reported",
        "distance_km",
        "area_covered_ha",
        "num_observers",
        "breeding_code",
        "observation_details",
        "comments",
        "ml_catalog_numbers",
    ]  # Note: column names as of 2021/09/14

    df.date = pd.to_datetime(df.date)

    df.sort_values("submission_id", ascending=False, inplace=True)
    logger.info("eBird observations successfully read and cleaned.")

    return df


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--file-path", type=str, default="data/MyEBirdData.csv")

    args = parser.parse_args()
    engine = create_engine(config.db_engine_str())

    df = read_and_clean_data(args.file_path)

    logger.info("Writing eBird observations to db...")
    df.to_sql("observations", engine, if_exists="replace")
    logger.info("Load of eBird observations complete!")
