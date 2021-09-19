"""Test cases for Streamlit app functionality."""
import pandas as pd
from sqlalchemy import create_engine

from ibyrd.app.streamlit import add_line_break
from ibyrd.util import config


def test_get_data():
    """Test for get_data function of Streamlit."""
    engine = create_engine(config.postgres_engine_str())  # TODO: Generalize
    """Testing api key extraction."""
    sql_query = """
    select t.*, o.date
    from taxonomy t
    left join observations o
    on o.taxon_order = t.taxon_order limit 10
    """
    df = pd.read_sql(sql_query, engine)
    assert len(df) == 10
    assert len(df.columns) == 17
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
