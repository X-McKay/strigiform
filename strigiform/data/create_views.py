"""Create views ontop of existing tables."""
from strigiform.platform.storage.rdbms import RDBMSProvider

import sqlalchemy

rdbms = RDBMSProvider()
engine = rdbms.get_engine()

# TODO: ONLY WORKS WITH POSTGRESQL
view_string = """
    CREATE OR REPLACE VIEW monthly_summary AS
    SELECT
        DATE_TRUNC('month', date) as "time",
        COUNT(DISTINCT date) as days_birded,
        COUNT(DISTINCT location) as unique_locations,
        COUNT(taxonomic_order) AS total_species_count,
        COUNT(DISTINCT taxonomic_order) as unique_species_count
    FROM observations
    WHERE
        EXTRACT(YEAR from date) >= 2019
    GROUP BY DATE_TRUNC('month', date)
    ORDER BY DATE_TRUNC('month', date) DESC
"""

sql_query = sqlalchemy.text(view_string)
result = engine.execute(sql_query)
