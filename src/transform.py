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

        
        if table == "stores":
            df["store_id"] = df.index
            name_to_id = dict(zip(df["name"], df["store_id"]))

        if table == "orders":
            date_columns = ["order_date", "required_date", "shipped_date"]
            df["store"] = df["store"].map(name_to_id)
            df = df.rename(columns={"store": "store_id"})
            df = reorder_dates(df, date_columns)

        if table == "staffs":
            df["store_name"] = df["store_name"].map(name_to_id)
            df = df.rename(columns={"store_name": "store_id"})
            df = df.drop("street", axis=1)

        if table == "stocks":
            df["store_name"] = df["store_name"].map(name_to_id)
            df = df.rename(columns={"store_name": "store_id"})

        write_to_staging(table, df)
    

def main():
    pass
    #df = pd.read_csv(config.ORDERS_FILE)
    #date_columns = ["order_date", "required_date", "shipped_date"]
    #df = reorder_dates(df, date_columns)

    #write_to_staging("orders", df)

    ##print(df)


if __name__ == "__main__":
    main()
