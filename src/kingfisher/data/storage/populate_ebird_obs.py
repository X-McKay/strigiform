"""Populate database tables."""
from sqlalchemy import create_engine

from kingfisher.data.ingest import ebird
from kingfisher.util import config

df = ebird.read_and_clean_data("data/MyEBirdData.csv")

engine = create_engine(config.postgres_engine_str())  # TODO: Generalize

df.to_sql("observations", engine, if_exists="replace")
