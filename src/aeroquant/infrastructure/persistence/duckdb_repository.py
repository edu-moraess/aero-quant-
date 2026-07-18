from pathlib import Path
from typing import Optional

import duckdb

class DuckDBRepository:
    def __init__(self, db_path: str = "data/aeroquant.duckdb"):
        self.db_path = db_path
        self._conn = None

    def __enter__(self):
        self._conn = duckdb.connect(self.db_path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._conn:
            self._conn.close()

    def execute(self, query: str) -> Optional[duckdb.DuckDBPyConnection]:
        if not self._conn:
            self._conn = duckdb.connect(self.db_path)
        return self._conn.execute(query)

    def save_dataframe(self, df, table_name: str) -> bool:
        if not self._conn:
            self._conn = duckdb.connect(self.db_path)
        self._conn.register("df", df)
        self._conn.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df")
        return True