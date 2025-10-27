from pathlib import Path
from dataclasses import dataclass, asdict


# Directories
BASE_DIR = Path(__file__).parent.parent.resolve()
RAW_DATA_DIR = BASE_DIR / "data/raw"
PROCESSED_DATA_DIR = BASE_DIR / "data/processed"
SRC_DIR = BASE_DIR / "src"
TESTS_DIR = BASE_DIR / "tests"
SQL_DIR = BASE_DIR / "sql"
SCHEMA_DIR = SQL_DIR / "schema"
STORED_PROCEDURES_DIR = SQL_DIR / "stored_procedures"
API_DIR = RAW_DATA_DIR / "api"

# Ensure directories exist
RAW_DATA_DIR.mkdir(exist_ok=True, parents=True)
PROCESSED_DATA_DIR.mkdir(exist_ok=True, parents=True)
SRC_DIR.mkdir(exist_ok=True, parents=True)
TESTS_DIR.mkdir(exist_ok=True, parents=True)
SQL_DIR.mkdir(exist_ok=True, parents=True)
SCHEMA_DIR.mkdir(exist_ok=True, parents=True)
STORED_PROCEDURES_DIR.mkdir(exist_ok=True, parents=True)
API_DIR.mkdir(exist_ok=True, parents=True)

# Files
RAW_FILES = {
    "customers": RAW_DATA_DIR / "api/customers.csv",
    "order_items": RAW_DATA_DIR / "api/order_items.csv",
    "orders": RAW_DATA_DIR / "api/orders.csv",
    "staffs": RAW_DATA_DIR / "csv/staffs.csv",
    "brands": RAW_DATA_DIR / "db/brands.csv",
    "categories": RAW_DATA_DIR / "db/categories.csv",
    "products": RAW_DATA_DIR / "db/products.csv",
    "stocks": RAW_DATA_DIR / "db/stocks.csv",
    "stores": RAW_DATA_DIR / "csv/stores.csv"
}

CUSTOMERS_FILE = RAW_DATA_DIR / "api/customers.csv"
ORDER_ITEMS_FILE = RAW_DATA_DIR / "api/order_items.csv"
ORDERS_FILE = RAW_DATA_DIR / "api/orders.csv"
STAFFS_FILE = RAW_DATA_DIR / "csv/staffs.csv"
STORES_FILE = RAW_DATA_DIR / "csv/stores.csv"
BRANDS_FILE = RAW_DATA_DIR / "db/brands.csv"
CATEGORIES_FILE = RAW_DATA_DIR / "db/categories.csv"
PRODUCTS_FILE = RAW_DATA_DIR / "db/products.csv"
STOCKS_FILE = RAW_DATA_DIR / "db/stocks.csv"

# API
API_ENDPOINTS = {
    "orders": "https://etl-server.fly.dev/orders",
    "order_items": "https://etl-server.fly.dev/order_items",
    "customers": "https://etl-server.fly.dev/customers",
}

URL_ORDERS = "https://etl-server.fly.dev/orders" 
URL_ORDER_ITEMS = "https://etl-server.fly.dev/order_items"
URL_CUSTOMERS = "https://etl-server.fly.dev/customers"

DB_NAME = "integrated_db"
DB_SCHEMA = SCHEMA_DIR / "baseline_integrated_db.sql"
DEPENDENCIES_PROCEDURE = STORED_PROCEDURES_DIR / "get_dependencies.sql"





@dataclass (frozen=True)
class DatabaseConnectionConfig:
    host: str
    port: int
    user: str
    password: str
    database: str | None


dbconfig = DatabaseConnectionConfig(host="localhost", port=3306, user="root", password="password", database=DB_NAME)
dbconfig_dict = asdict(dbconfig)