from pathlib import Path
from dataclasses import dataclass, asdict


# Directories
BASE_DIR = Path(__file__).parent.parent.resolve()
RAW_DATA_DIR = BASE_DIR / "data/raw"
PROCESSED_DATA_DIR = BASE_DIR / "data/processed"
SRC_DIR = BASE_DIR / "src"
TESTS_DIR = BASE_DIR / "tests"
SCHEMA_DIR = BASE_DIR / "schema"

# Ensure directories exist
RAW_DATA_DIR.mkdir(exist_ok=True, parents=True)
PROCESSED_DATA_DIR.mkdir(exist_ok=True, parents=True)
SRC_DIR.mkdir(exist_ok=True, parents=True)
TESTS_DIR.mkdir(exist_ok=True, parents=True)

# Files
CUSTOMERS_FILE = RAW_DATA_DIR / "api/data/customers.csv"
ORDER_ITEMS_FILE = RAW_DATA_DIR / "api/data/order_items.csv"
ORDERS_FILE = RAW_DATA_DIR / "api/data/orders.csv"
STAFFS_FILE = RAW_DATA_DIR / "csv/staffs.csv"
STORES_FILE = RAW_DATA_DIR / "csv/stores.csv"
BRANDS_FILE = RAW_DATA_DIR / "db/brands.csv"
CATEGORIES_FILE = RAW_DATA_DIR / "db/categories.csv"
PRODUCTS_FILE = RAW_DATA_DIR / "db/products.csv"
STOCKS_FILE = RAW_DATA_DIR / "db/stocks.csv"

# API
URL_ORDERS = "https://etl-server.fly.dev/orders" 
URL_ORDER_ITEMS = "https://etl-server.fly.dev/order_items"
URL_CUSTOMERS = "https://etl-server.fly.dev/customers"

DB_NAME = "integrated_db"
DB_SCHEMA = SCHEMA_DIR / "create_final_db.sql"





@dataclass (frozen=True)
class DatabaseConnectionConfig:
    host: str
    port: int
    user: str
    password: str
    database: str | None


dbconfig = DatabaseConnectionConfig(host="localhost", port=3306, user="root", password="password", database=DB_NAME)
dbconfig_dict = asdict(dbconfig)