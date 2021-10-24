"""Test cases for Streamlit app functionality."""
import sqlite3
import unittest

import pandas as pd

from kingfisher.app.streamlit import add_line_break
from kingfisher.app.streamlit import get_data
from kingfisher.app.streamlit import get_period_stats


class Streamlit(unittest.TestCase):
    """Testing class."""

    def get_test_data(self):
        """Test data select."""
        self.conn = sqlite3.connect("./tests/mock_db.db")
        # Read mock data and insert into mock db
        test_data = pd.read_csv("./tests/mock_data.csv")
        test_data.to_sql("mock_data", self.conn, if_exists="replace")
        sql_query = """select * from mock_data"""
        self.df = get_data(sql_query, self.conn)

    def test_get_data(self):
        """Test for get_data function of Streamlit."""
        self.get_test_data()
        sql_query = """select * from mock_data"""
        df = get_data(sql_query, self.conn)

        assert len(df) == 10
        assert len(df.columns) == 20

    def test_get_period_stats_date(self):
        """Test for retreiving period statistics."""
        self.get_test_data()
        with self.assertRaises(ValueError):
            get_period_stats(
                self.df, pd.to_datetime("2021-02-01"), pd.to_datetime("2021-01-01")
            )

    def test_get_period_stats_df(self):
        """Test for retreiving period statistics."""
        mock_df = pd.DataFrame()
        with self.assertRaises(ValueError):
            get_period_stats(
                mock_df, pd.to_datetime("2021-01-01"), pd.to_datetime("2021-02-01")
            )

    def test_add_line_break(self):
        """Test for generic line break."""
        assert add_line_break() is not None
