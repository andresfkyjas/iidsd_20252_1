
import pandas as pd
from sqlite3 import connect

import platform

class Database:
    def __init__(self, db_path=":memory:"):
        self.db_path = db_path
        # Detecta si es Windows
        self.ok_symbol = "[OK]" if platform.system() == "Windows" else "✅"

    def create_table(self, df: pd.DataFrame, table_name: str, if_exists="replace"):
        with connect(self.db_path) as conn:
            df.to_sql(table_name, conn, if_exists=if_exists, index=False)
            print(f"{self.ok_symbol} Tabla '{table_name}' creada en {self.db_path}")