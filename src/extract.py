import time
from pathlib import Path

import pandas as pd
#import polars as pl

import config


def read_url_write_csv(url: str, path: Path) -> None:
    df = pd.read_json(url)
    df.to_csv(path, index=False)


def extract_all_sources() -> None:
    
    read_url_write_csv(config.URL_CUSTOMERS, config.RAW_DATA_DIR / "api" /"customers.csv")
    read_url_write_csv(config.URL_ORDER_ITEMS, config.RAW_DATA_DIR / "api" / "order_items.csv")
    read_url_write_csv(config.URL_ORDERS, config.RAW_DATA_DIR / "api" / "orders.csv")


if __name__ == "__main__":
    start_time = time.time()
    extract_all_sources()
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.2f}s")
