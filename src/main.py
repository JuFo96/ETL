import numpy as np
import pandas as pd

import config
import utils
from schema import Schema
from connection import DatabaseConnection
from table import Table


def main():
    # staff_translation = {"name": "staff_first_name", "last_name": "staff_first_name"}
    # data = config.RAW_DATA_DIR / "csv" / "staffs.csv"

    integrated_db = Schema(schema_file_path=config.DB_SCHEMA)
    table_names = integrated_db.get_tables()
    
    tables = {}

    with DatabaseConnection(config=config.dbconfig) as connection:
        #graph = utils.get_table_dependencies(sql_procedure_path=config.DEPENDENCIES_PROCEDURE, connection=connection)
        #print(graph)
        #for table in table_names:
        #    tables[table] = Table(table_name=table, connection=connection)
        #    tables[table].insertmany()
        integrated_db.run_sql_schema(connection)
        order_items = Table(table_name="order_items", connection=connection)
        brands = Table(table_name="brands", connection=connection)
        categories = Table(table_name="categories", connection=connection)
        products = Table(table_name="products", connection=connection)
        stocks = Table(table_name="stocks", connection=connection)
        orders = Table(table_name="orders", connection=connection)
        customers = Table(table_name="customers", connection=connection)
        staffs = Table(table_name="staffs", connection=connection)
        stores = Table(table_name="stores", connection=connection)

        order_items_data = pd.read_csv(config.ORDER_ITEMS_FILE).to_dict("records")
        brands_data = pd.read_csv(config.BRANDS_FILE).to_dict("records")
        categories_data = pd.read_csv(config.CATEGORIES_FILE).to_dict("records")
        products_data = pd.read_csv(config.PRODUCTS_FILE).to_dict("records")

        stocks_data = pd.read_csv(config.STOCKS_FILE).to_dict("records")
        orders_data = (
            pd.read_csv(config.ORDERS_FILE).convert_dtypes().to_dict("records")
        )

        ##orders_data = orders_data.to_dict("records")
        customers_data = (
            pd.read_csv(config.CUSTOMERS_FILE)
            .replace({np.nan: None})
            .to_dict("records")
        )
        staffs_data = (
            pd.read_csv(config.STAFFS_FILE).replace({np.nan: None}).to_dict("records")
        )
        stores_data = (
            pd.read_csv(config.STORES_FILE).replace({np.nan: None}).to_dict("records")
        )

        

        # No children
        brands.insertmany(data=brands_data)
        categories.insertmany(data=categories_data)
        stores.insertmany(data=stores_data)
        customers.insertmany(data=customers_data)
        staffs.insertmany(data=staffs_data)

        products.insertmany(data=products_data)

        stocks.insertmany(data=stocks_data)

        orders.insertmany(data=orders_data)
        order_items.insertmany(data=order_items_data)


if __name__ == "__main__":
    main()
