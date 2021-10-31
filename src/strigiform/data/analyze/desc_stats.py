"""Fetch descriptive statistics."""
import pandas as pd
from sqlalchemy import create_engine

from strigiform.util import config
from strigiform.util import logger

logger = logger.logger_init(name=__name__)

engine = create_engine(config.db_engine_str())  # TODO: Generalize


def get_ll_stats():
    """Placeholder trash."""
    sql_query = """
        select *
        from taxonomy t
        where t.taxon_order in
        (select distinct taxon_order from observations)
        """

    df = pd.read_sql(sql_query, engine)

    num_orders = df.order_name.nunique()
    num_families = df.family_sci_name.nunique()

    print("Orders:", num_orders)
    print("Families:", num_families)
    # return num_orders, num_families

    if __name__ == "__main__":
        get_ll_stats()
