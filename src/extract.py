import time
from pathlib import Path

import pandas as pd


import config


def read_url_write_csv(url: str, path: Path) -> None:
    """Reads json contents with pandas and writes to a csv.

    Args:
        url: Url of the given API.
        path: Output path where csv is written to.
    """
    df = pd.read_json(url)
    df.to_csv(path, index=False)


def extract_all_sources() -> None:
    """Wrapper function to loop over APIs in defined in config.py"""
    for api, url in config.API_ENDPOINTS.items():
        read_url_write_csv(url, config.RAW_DATA_DIR / "api" / f"{api}.csv")
    


if __name__ == "__main__":
    start_time = time.time()
    extract_all_sources()
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.2f}s")
