import uuid
from pathlib import Path
from typing import Iterable
import pandas as pd

import config


def reorder_dates(df: pd.DataFrame, date_columns: list) -> pd.DataFrame:
    df[date_columns] = df[date_columns].apply(pd.to_datetime, dayfirst=True)
    return df

def write_to_staging(table_name: str, df: pd.DataFrame) -> None:
    return df.to_csv(config.PROCESSED_DATA_DIR / f"{table_name}.csv", index=False)

def transform_all_tables(tables: dict[str, Path]) -> None:
    for table in tables:
        df = pd.read_csv(tables[table])

        if table == "orders":
            date_columns = ["order_date", "required_date", "shipped_date"]
            df = reorder_dates(df, date_columns)

        write_to_staging(table, df)
    

def main():
    df = pd.read_csv(config.ORDERS_FILE)
    date_columns = ["order_date", "required_date", "shipped_date"]
    df = reorder_dates(df, date_columns)

    write_to_staging("orders", df)

    print(df)


if __name__ == "__main__":
    main()
