from pathlib import Path
from dataclasses import dataclass, asdict


# Directories
BASE_DIR = Path(__file__).parent.parent.resolve()
RAW_DATA_DIR = BASE_DIR / "data/raw"
PROCESSED_DATA_DIR = BASE_DIR / "data/processed"
SRC_DIR = BASE_DIR / "src"
TESTS_DIR = BASE_DIR / "tests"
SCHEMA_DIR = BASE_DIR / "schema"

# Files


RAW_DATA_DIR.mkdir(exist_ok=True, parents=True)
PROCESSED_DATA_DIR.mkdir(exist_ok=True, parents=True)
SRC_DIR.mkdir(exist_ok=True, parents=True)
TESTS_DIR.mkdir(exist_ok=True, parents=True)

DB_NAME = "integrated_db"
DB_SCHEMA = SCHEMA_DIR / "create_final_db.sql"



@dataclass (frozen=True)
class DatabaseConnectionConfig:
    host: str
    port: int
    user: str
    password: str
    database: str | None


dbconfig = DatabaseConnectionConfig("localhost", 3306, "root", "password", DB_NAME)
dbconfig_dict = asdict(dbconfig)