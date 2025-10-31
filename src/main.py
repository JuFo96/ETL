import pandas as pd

import config
import utils
from connection import DatabaseConnection
from schema import Schema
from table import Table
from extract import extract_all_sources
from transform import transform_all_tables
import time


def setup_db(database: Schema, connection: DatabaseConnection) -> list[str]:
    database.run_sql_schema(connection)
    insert_order = utils.get_insert_order(
            sql_procedure_path=config.DEPENDENCIES_PROCEDURE, connection=connection
        )
    return insert_order

def load_db(database: Schema, connection: DatabaseConnection) -> None:
    """Does something"""
    insert_order = setup_db(database, connection)
    
    tables: dict[str, Table] = {}
    
    for table in insert_order:
        print(table)

        columns = set(database.get_columns(table))
        tables[table] = Table(
            table_name=table, connection=connection, valid_columns=columns
        )
        data = pd.read_csv(config.PROCESSED_DATA_DIR / f"{table}.csv")

        data = data.to_dict("records")

        tables[table].insertmany(data)


def main():
    extract_all_sources()
    transform_all_tables(config.RAW_FILES)

    integrated_db = Schema(schema_file_path=config.DB_SCHEMA)
    with DatabaseConnection(config=config.dbconfig) as connection:
        load_db(integrated_db, connection)



if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Elapsed time: {end - start:.2f}s")