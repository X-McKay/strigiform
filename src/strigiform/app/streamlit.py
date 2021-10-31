"""Module for basic Streamlit webapps."""
import datetime
from datetime import timedelta

import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

from strigiform.app import queries
from strigiform.util import config
from strigiform.util import logger

logger = logger.logger_init(name=__name__)


# Global streamlit consifurations
st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 250px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 250px;
        margin-left: -250px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def add_line_break():
    """Generic function to add line break."""
    return st.markdown(
        """
    \
     -----"""
    )


def get_data(sql_query, engine) -> pd.DataFrame:
    """Query observational data."""
    logger.info("Querying database for taxonomy and observations...")
    df = pd.read_sql(sql_query, engine)
    if len(df) < 1:
        logger.error("No data found")
        raise ValueError("No data found.")
    if "date" not in df.columns:
        logger.error("No date column.")
        raise AttributeError("No date column.")

    df["date"] = pd.to_datetime(df["date"])
    df["date"] = df["date"].dt.date
    logger.info("Query complete!")
    return df


def get_period_stats(df: pd.DataFrame, start: datetime, end: datetime) -> None:
    """Create descriptive statisic widgets of observations over a period.

    :param df: Dataframe of birding observations.
    :type df: Pandas DataFrame
    :param start: Start date of observation window.
    :type start: datetime
    :param end: End date of observation window.
    :type end: datetime
    """
    if start >= end:
        raise ValueError("Start date must be before end date.")

    col_check_list = ["date", "order_name", "family_sci_name", "taxon_order"]
    for col in col_check_list:
        if col not in df.columns:
            logger.error(f"No {col} column.")
            raise AttributeError(f"No {col} column.")
    try:
        period_df = df[(df.date >= start) & (df.date <= end)]

        left_column, right_column = st.columns(2)

        with left_column:
            st.write("Unique Orders:", period_df.order_name.nunique())
            st.write("Unique Families:", period_df.family_sci_name.nunique())
        with right_column:
            st.write("Unique Species:", period_df.taxon_order.nunique())

    except Exception as e:
        logger.error(e)
        raise e


def get_period_species(
    df: pd.DataFrame, start: datetime, end: datetime
) -> pd.DataFrame:
    """Get table of unique species over a period of time.

    :param df: Dataframe of birding observations.
    :type df: Pandas DataFrame
    :param start: Start date of observation window.
    :type start: datetime
    :param end: End date of observation window.
    :type end: datetime
    :return: Subset or input dataframe with unique species
    :rtype: Pandas DataFrame
    """
    period_df = df[(df.date >= start) & (df.date <= end)]
    species_df = period_df[
        ["order_name", "family_com_name", "scientific_name", "common_name"]
    ]
    species_df.drop_duplicates(inplace=True)
    species_df.reset_index(drop=True, inplace=True)
    return species_df


def main():
    """Main application script."""
    # Set default end date as Today
    today = datetime.date.today()

    # Extract data using default engine
    engine = create_engine(config.db_engine_str())  # TODO: Generalize
    df = get_data(queries.observation_query, engine)

    # Get list of unique orders for multiselect widget
    order_list = list(df.order_name.unique())
    order_list.sort()

    # Configure sidebar and sidebar widgets
    st.sidebar.markdown("## Select a date range")
    start = st.sidebar.date_input("Start date", today - timedelta(days=365))
    end = st.sidebar.date_input("End date", today)

    # Multiselect to subset to one or more orders
    order_select = st.sidebar.multiselect(
        "Explore by order:",
        order_list,
        default=None,
        help="If no specific orders are selected, all orders will be included.",
    )

    # Default to all orders if multiselect is empty
    if len(order_select) < 1:
        app_df = df
    else:
        app_df = df[df.order_name.isin(order_select)]

    # Configure main app content
    st.title("iByrd: Panorama")

    left_column, right_column = st.columns(2)

    # Display date selections
    with left_column:
        st.write("Start date:", start)
    with right_column:
        st.write("End date:", end)
    add_line_break()

    # Summary statistics
    st.markdown("### Summary Statistics:")
    get_period_stats(app_df, start, end)
    add_line_break()

    # DataFrame of observations
    st.dataframe(get_period_species(app_df, start, end))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(e)
        raise TypeError from e
