import re
from pathlib import Path


import config


class Schema:
    def __init__(self, schema_file_path: Path) -> None:
        self.file_path = schema_file_path
        self.tables = {}
        self.parse_schema_regex()

    def _read_file(self) -> str:
        with open(file=self.file_path, mode='r') as f:
            return f.read()
    

    def parse_schema_regex(self) -> None:
        """Parses a schema file to extract table and column names with RegEx."""
        content = self._read_file()

        # Match CREATE TABLE ... (...);
        # Uses non-greedy .*? to stop at first matching )
        pattern = r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?`?(\w+)`?\s*\((.*?)\);"

        for match in re.finditer(pattern, content, re.DOTALL | re.IGNORECASE):
            table_name = match.group(1)
            columns_section = match.group(2)

            # Extract column names from the columns section
            # Match word at start of line (column name) followed by type
            column_pattern = r"^\s*`?(\w+)`?\s+(?:INT|VARCHAR|TEXT|real|DATETIME|DECIMAL|BOOLEAN|BIGINT|SMALLINT|FLOAT|DOUBLE|DATE|TIME|TIMESTAMP|CHAR|BLOB)"

            columns = []
            for line in columns_section.split("\n"):
                col_match = re.match(column_pattern, line.strip(), re.IGNORECASE)
                if col_match:
                    columns.append(col_match.group(1))

            self.tables[table_name] = columns



    def run_sql_schema(self, connection) -> None:
        """Reads a schema file and executes commands sequentially split by ;

        Args:
            Connection to a database
        """
        content = self._read_file()
        with connection.cursor() as cur:
            for statement in content.split(";"):
                statement = statement.strip()
                if statement:
                    cur.execute(statement)
            connection.commit()


    def get_tables(self) -> list[str]:
        """Returns a list of table names"""
        return list(self.tables.keys())

    def get_columns(self, table_name: str) -> list:
        """Returns a list of column names per table.
        
        Args:
            table_name: table name from schema

        Returns:
            A list of column names for the given table. 
        """
        return self.tables[table_name]

    def get_all_columns(self) -> set[str]:
        """Returns all column names in the database schema"""
        all_cols = []
        for columns in self.tables.values():
            all_cols.extend(columns)
        return set(all_cols)

def main() -> None:
    schema1 = Schema(schema_file_path=config.DB_SCHEMA)
    print(schema1.tables)


if __name__ == "__main__":
    main()
