import pandas as pd

import config
import utils
from connection import DatabaseConnection
from schema import Schema
from table import Table


def main():
    integrated_db = Schema(schema_file_path=config.DB_SCHEMA)

    with DatabaseConnection(config=config.dbconfig) as connection:
        integrated_db.run_sql_schema(connection)
        insert_order = utils.get_insert_order(
            sql_procedure_path=config.DEPENDENCIES_PROCEDURE, connection=connection
        )

        tables = {}
        for table in insert_order:
            columns = set(integrated_db.get_columns(table))
            tables[table] = Table(
                table_name=table, connection=connection, valid_columns=columns
            )
            data = pd.read_csv(config.PROCESSED_DATA_DIR / f"{table}.csv")
            data = data.convert_dtypes().to_dict("records")
            tables[table].insertmany(data)


if __name__ == "__main__":
    main()
