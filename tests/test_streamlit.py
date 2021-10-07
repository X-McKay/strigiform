"""Test cases for Streamlit app functionality."""
import sqlite3

import pandas as pd

from ibyrd.app.streamlit import add_line_break


# TODO: Clean up testing and restructure as class


def test_get_data():
    """Test for get_data function of Streamlit."""
    # Initialize in-memory db
    conn = sqlite3.connect("./tests/mock_db.db")

    # Read mock data and insert into mock db
    test_data = pd.read_csv("./tests/mock_data.csv")
    test_data.to_sql("mock_data", conn, if_exists="replace")

    sql_query = """select * from mock_data"""

    df = pd.read_sql(sql_query, conn)
    assert len(df) == 10
    assert len(df.columns) == 19
    return df


def test_get_period_stats():
    """Test for retreiving period statistics."""
    df = test_get_data()
    assert df.order_name.nunique() > 0
    assert df.family_sci_name.nunique() > 0
    assert df.taxon_order.nunique() > 0


# TODO: NEED TO INVESTIGATE
# def test_get_period_species():
#         df = test_get_data()
#         print(df.shape)
#         species_df = get_period_species(df.copy(), df.date.max(), df.date.max())
#         print(df.shape)
#         assert(len(species_df) > 0)
#         assert(len(species_df) <= len(df))
#         assert(len(species_df.columns) == 4)


def test_add_line_break():
    """Test for generic line break."""
    assert add_line_break() is not None
