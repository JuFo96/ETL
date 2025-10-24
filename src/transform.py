import uuid
import pandas as pd
import config
from pathlib import Path

def reorder_dates(date_column: pd.Series) -> pd.Series:
    
    return date_column

def write_to_staging(df: pd.DataFrame, file_path: Path) -> None:
    return df.to_csv(file_path / "orders.csv", index=False)

def main():
    df = pd.read_csv(config.ORDERS_FILE)
    date_columns = ["order_date", "required_date", "shipped_date"]
    df[date_columns] = df[date_columns].apply(pd.to_datetime, dayfirst=True)
    write_to_staging(df, config.PROCESSED_DATA_DIR)





    print(df)




if __name__ == "__main__":
    main()