"""Create database tables for storing information."""
import psycopg2

from kingfisher.util import config


def create_tables(db_config=config.postgres_config):
    """Create tables in the PostgreSQL database."""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS taxonomy (
            scientific_name VARCHAR(255) NOT NULL,
            common_name VARCHAR(255) NOT NULL,
            species_code VARCHAR(255) NOT NULL,
            category VARCHAR(255) NOT NULL,
            taxon_order INTEGER PRIMARY KEY UNIQUE,
            com_name_codes VARCHAR(255) NOT NULL,
            sci_name_codes VARCHAR(255) NOT NULL,
            banding_codes VARCHAR(255) NOT NULL,
            order_name VARCHAR(255) NOT NULL,
            family_com_name VARCHAR(255) NOT NULL,
            family_sci_name VARCHAR(255) NOT NULL,
            report_as FLOAT,
            extinct BOOLEAN,
            extinct_year VARCHAR(4),
            family_code VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE IF NOT EXISTS test (
                part_id SERIAL PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL
                )
        """,
    )
    conn = None
    try:
        # read the connection parameters
        params = db_config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    create_tables()
