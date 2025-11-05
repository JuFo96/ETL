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


RAW_FILES = {
    "brands": RAW_DATA_DIR / "db/brands.csv",
    "categories": RAW_DATA_DIR / "db/categories.csv",
    "stores": RAW_DATA_DIR / "csv/stores.csv",
    "orders": RAW_DATA_DIR / "api/orders.csv",
    "customers": RAW_DATA_DIR / "api/customers.csv",
    "products": RAW_DATA_DIR / "db/products.csv",
    "staffs": RAW_DATA_DIR / "csv/staffs.csv",   
    "order_items": RAW_DATA_DIR / "api/order_items.csv",
    "stocks": RAW_DATA_DIR / "db/stocks.csv",
}

API_ENDPOINTS = {
    "orders": "https://etl-server.fly.dev/orders",
    "order_items": "https://etl-server.fly.dev/order_items",
    "customers": "https://etl-server.fly.dev/customers",
}



DB_NAME = "bikestore_db"
DB_SCHEMA = SCHEMA_DIR / "psql_integrated_db.sql"
DEPENDENCIES_PROCEDURE = STORED_PROCEDURES_DIR / "get_dependencies.sql"





@dataclass (frozen=True)
class DatabaseConnectionConfig:
    host: str
    port: int
    user: str
    password: str
    dbname: str | None


dbconfig = DatabaseConnectionConfig(host="localhost", port=5432, user="etl_app", password="password", dbname=DB_NAME)
dbconfig_dict = asdict(dbconfig)