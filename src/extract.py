import time
from pathlib import Path

import pandas as pd


import config


def read_url_write_csv(url: str, path: Path) -> None:
    df = pd.read_json(url)
    df.to_csv(path, index=False)


def extract_all_sources() -> None:
    for api, url in config.API_ENDPOINTS.items():
        read_url_write_csv(url, config.RAW_DATA_DIR / "api" / f"{api}.csv")
    


if __name__ == "__main__":
    start_time = time.time()
    extract_all_sources()
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.2f}s")
