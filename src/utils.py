from pathlib import Path

import pandas as pd
import mysql.connector
import config
from dataclasses import asdict


def transform_column_names(file: Path, name_translation: dict):
    
    data = pd.read_csv(file)
    #print(data.columns)
    renamed_df = data.rename(columns=name_translation)
    
    return renamed_df

def print_column_names():
    pass





def run_sql_schema(file: Path, connection) -> None:
    with open(file, "r") as f:
        sql = f.read()
    with connection.cursor() as cur:
        for statement in sql.split(";"):
            statement = statement.strip()
            if statement:
                cur.execute(statement)
        connection.commit()







def main():
    #staff_translation = {"name": "staff_first_name", "last_name": "staff_first_name"}
    #data = config.RAW_DATA_DIR / "csv" / "staffs.csv"
    
    db_cred = asdict(config.dbconfig) 
    connection = mysql.connector.connect(**db_cred)
    print(connection.is_connected())
    run_sql_schema(config.DB_SCHEMA, connection=connection)
    

    #print(df.columns)






if __name__ == "__main__":
    main()