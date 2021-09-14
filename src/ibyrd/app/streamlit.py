"""Module for basic Streamlit webapps."""
import datetime

import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

from ibyrd.util import config


st.sidebar.markdown("## Select a date range")
st.title("iByrd Eagle eye")

left_column, right_column = st.columns(2)

start = st.sidebar.date_input("Select start date", datetime.date(2018, 1, 1))
end = st.sidebar.date_input("Selet end date", datetime.date.today())

with left_column:
    st.write("Selected start date:", start)

with right_column:
    st.write("Selected end date:", end)


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


# Title the app


df = get_data()
st.dataframe(get_period_stats(df, start, end))
st.dataframe(get_period_species(df, start, end))

# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)
