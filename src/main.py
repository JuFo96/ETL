import config
import utils
from connection import DatabaseConnection
from table import Table
import pandas as pd


def main():
    # staff_translation = {"name": "staff_first_name", "last_name": "staff_first_name"}
    # data = config.RAW_DATA_DIR / "csv" / "staffs.csv"

    with DatabaseConnection(config.dbconfig) as connection:
        print(connection.is_connected())
        order_items = Table("customers", connection)

        order_items_data = pd.read_csv(config.RAW_DATA_DIR / "api" / "data" / "order_items.csv").to_dict("records")
        
        utils.run_sql_schema(config.DB_SCHEMA, connection=connection)
        order_items.insertmany(order_items_data)

if __name__ == "__main__":
    main()
