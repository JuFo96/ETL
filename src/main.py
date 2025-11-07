import time

import pandas as pd
from psycopg import sql
import config
import utils
from connection import DatabaseConnection
from extract import extract_all_sources
from schema import Schema
from table import Table
from transform import transform_all_tables


def load_db(database: Schema, connection: DatabaseConnection) -> None:
    """Does something"""
    insert_order = utils.get_insert_order(
        sql_procedure_path=config.DEPENDENCIES_PROCEDURE, connection=connection
    )

    tables: dict[str, Table] = {}
    for table in insert_order:
        columns = set(database.get_columns(table))
        tables[table] = Table(
            table_name=table, connection=connection, valid_columns=columns
        )
        data = pd.read_parquet(config.PROCESSED_DATA_DIR / f"{table}.parquet")

        data = data.to_dict("records")

        tables[table].insertmany(data)


def main():
    extract_all_sources()
    transform_all_tables(config.RAW_FILES)

    bikestore_db = Schema(schema_file_path=config.DB_SCHEMA)
    with DatabaseConnection(config=config.dbconfig) as connection:
        with connection.cursor() as cur:
            # Removes all data on the tables in bikestore
            cur.execute("""CALL bikestore.truncate_data_tables();""")
            cur.execute("set search_path to bikestore;")
        load_db(bikestore_db, connection)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Elapsed time: {end - start:.2f}s")
