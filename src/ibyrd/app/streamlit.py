"""Module for basic Streamlit webapps."""
import datetime
from datetime import timedelta

import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

from ibyrd.util import config


st.sidebar.markdown("## Select a date range")
st.title("iByrd: Panorama")

left_column, right_column = st.columns(2)

today = datetime.date.today()

start = st.sidebar.date_input("Start date", today - timedelta(days=365))
end = st.sidebar.date_input("End date", today)

with left_column:
    st.write("Start date:", start)

with right_column:
    st.write("End date:", end)


st.markdown(
    """
            \
            -----"""
)


st.markdown("### Summary Statistics:")

engine = create_engine(config.postgres_engine_str())  # TODO: Generalize


def get_data():
    """Query observational data."""
    sql_query = """
    select t.*, o.date
    from taxonomy t
    left join observations o
    on o.taxon_order = t.taxon_order
    """

    df = pd.read_sql(sql_query, engine)
    df.date = df.date.dt.date
    return df


def get_period_stats(df, start, end):
    """Get statistics over a specific period of time."""
    period_df = df[(df.date >= start) & (df.date <= end)]

    left_column, right_column = st.columns(2)

    with left_column:
        st.write("Unique Orders:", period_df.order_name.nunique())
        st.write("Unique Families:", period_df.family_sci_name.nunique())
    with right_column:
        st.write("Unique Species:", period_df.taxon_order.nunique())


def get_period_species(df, start, end):
    """Get table of unique species over a period of time."""
    period_df = df[(df.date >= start) & (df.date <= end)]
    species_df = period_df[
        ["order_name", "family_com_name", "scientific_name", "common_name"]
    ]
    species_df.drop_duplicates(inplace=True)
    species_df.reset_index(drop=True, inplace=True)
    return species_df


df = get_data()
get_period_stats(df, start, end)

st.markdown(
    """
            \
            -----"""
)

st.dataframe(get_period_species(df, start, end))
