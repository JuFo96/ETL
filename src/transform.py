import uuid
from pathlib import Path
import pandas as pd

import config


def reorder_dates(df: pd.DataFrame, date_columns: list) -> pd.DataFrame:
    """Changes date formt to yyyy-mm-dd
    
    Args:
        df: dataframe containing raw data
        date_columns: List of column names in df to perform operation on
        
    Returns:
        A dataframe with transformation applied
    """
    df[date_columns] = df[date_columns].apply(pd.to_datetime, dayfirst=True)
    return df

def write_to_staging(table_name: str, df: pd.DataFrame) -> None:
    """Writes parquet files with no index

    Args:
        table_name: The table to write
        df: dataframe corresponding to table_name
    """
    return df.to_parquet(config.PROCESSED_DATA_DIR / f"{table_name}.parquet", index=False)

def transform_all_tables(tables: dict[str, Path]) -> None:
    """Orchestrator function to transform all raw .csv files to .parquet with transformations
    and move to staging folder.

    Args: 
        tables: dictionary containing path of all raw csv files
    """
    for table in tables:
        df = pd.read_csv(tables[table])

        
        if table == "stores":
            # Pandas is 0 indexed, add + 1 to match id range of other tables.
            df["store_id"] = df.index + 1
            name_to_id = dict(zip(df["name"], df["store_id"]))

        if table == "orders":
            date_columns = ["order_date", "required_date", "shipped_date"]
            df["store"] = df["store"].map(name_to_id)
            df = df.rename(columns={"store": "store_id"})
            df = reorder_dates(df, date_columns)

        if table == "staffs":
            df["store_name"] = df["store_name"].map(name_to_id)
            df["manager_id"] = df["manager_id"].astype("Int64")
            df = df.rename(columns={"store_name": "store_id"})
            df = df.drop("street", axis=1)

        if table == "stocks":
            df["store_name"] = df["store_name"].map(name_to_id)
            df = df.rename(columns={"store_name": "store_id"})
        df = df.convert_dtypes()
        write_to_staging(table, df)
    

def main():
    pass


if __name__ == "__main__":
    main()
