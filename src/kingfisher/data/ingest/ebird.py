"""Placeholder for functionality to import personal checklists."""
import argparse

import pandas as pd


def read_and_clean_data(file_path):
    """Read Ebird csv export to a pandas DataFrame.

    :param args: file path
    :type args: string
    :return: Ebird extract of personal submissions
    :rtype: pandas DataFrame
    """
    df = pd.read_csv(file_path)

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

    return df


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--file-path", type=str, default="data/MyEBirdData.csv")

    args = parser.parse_args()

    df = read_and_clean_data(args.file_path)

    # Note: Quick tests/qa
    print(df.head())
