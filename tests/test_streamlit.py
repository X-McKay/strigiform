"""Test cases for Streamlit app functionality."""
import sqlite3

import pandas as pd
import unittest

from kingfisher.app.streamlit import get_data
from kingfisher.app.streamlit import add_line_break
from kingfisher.app.streamlit import get_period_stats





    
class Streamlit(unittest.TestCase):
    
    def get_test_data(self):
        self.conn = sqlite3.connect("./tests/mock_db.db")
        # Read mock data and insert into mock db
        test_data = pd.read_csv("./tests/mock_data.csv")
        test_data.to_sql("mock_data", self.conn, if_exists="replace")
        sql_query = """select * from mock_data"""
        self.df = get_data(sql_query, self.conn)

    
    def test_get_data(self):
        self.get_test_data()
        sql_query = """select * from mock_data"""
        df = get_data(sql_query, self.conn)
        """Test for get_data function of Streamlit."""
        assert len(df) == 10
        assert len(df.columns) == 20
        
    def test_get_period_stats_date(self):
        self.get_test_data()
        """Test for retreiving period statistics."""
        with self.assertRaises(ValueError):
            get_period_stats(self.df, pd.to_datetime('2021-02-01'), pd.to_datetime('2021-01-01'))
            
    def test_get_period_stats_df(self):
        mock_df = pd.DataFrame()
        """Test for retreiving period statistics."""
        with self.assertRaises(ValueError):
            get_period_stats(mock_df, pd.to_datetime('2021-01-01'), pd.to_datetime('2021-02-01'))
            
    def test_add_line_break(self):
        """Test for generic line break."""
        assert add_line_break() is not None
    

# @pytest.fixture
# class StreamlitTest:
    
#     def __init__(
#         self, 
#         conn = conn,
#         df = df,
#     ):
#         """Initialize TestCase."""
#         self.conn = conn
#         self.df = df
    
#     @pytest.fixture
#     def test_get_data():
#         sql_query = """select * from mock_data"""
#         df = get_data(sql_query, conn)
#         """Test for get_data function of Streamlit."""
#         self.assertEqual(len(df), 10)
#         self.assertEqual(len(df.columns), 20)


#     def test_get_period_stats(self):
#         """Test for retreiving period statistics."""
#         with self.assertRaises(ValueError):
#             get_period_stats(self.df, pd.to_datetime('2021-02-01'), pd.to_datetime('2021-01-01'))
            
#     def test_add_line_break(self):
#         """Test for generic line break."""
#         assert add_line_break() is not None
    


# # TODO: NEED TO INVESTIGATE
# # def test_get_period_species():
# #         df = test_get_data()
# #         print(df.shape)
# #         species_df = get_period_species(df.copy(), df.date.max(), df.date.max())
# #         print(df.shape)
# #         assert(len(species_df) > 0)
# #         assert(len(species_df) <= len(df))
# #         assert(len(species_df.columns) == 4)



    

