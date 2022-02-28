"""Populate database tables with ebird observations."""
import argparse
from strigiform.data.model.observations import observations as obs_model
from strigiform.platform.storage.rdbms import RDBMSProvider
from strigiform.util import logger
from typing import List

import pandas as pd
from sqlmodel import Session
from sqlmodel import SQLModel


logger = logger.logger(name=__name__)


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
        "taxonomic_order",
        "count",
        "state_province",
        "county",
        "location_id",
        "location",
        "latitude",
        "longitude",
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


def df_to_sqlmodel(df: pd.DataFrame) -> List[SQLModel]:
    """Convert a pandas DataFrame into a a list of SQLModel objects."""
    obs = [obs_model(**row) for row in df.to_dict("records")]
    logger.info(f"Loaded {len(obs)} observations into SQLModel.")
    return obs


def load_observations(obs):
    """Load observations into the database."""
    rdbms = RDBMSProvider()
    engine = rdbms.get_engine()

    session = Session(engine)

    for o in obs:
        session.add(o)
    session.commit()
    session.close()

    logger.info("Observations successfully loaded into database.")


if __name__ == "__main__":
    """Main executable."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--file-path", type=str, default="./data/MyEBirdData.csv")

    args = parser.parse_args()

    df = read_and_clean_data(args.file_path)
    obs = df_to_sqlmodel(df)
    load_observations(obs)
    logger.info("Bulk load complete!")
