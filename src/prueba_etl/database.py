
import pandas as pd
from sqlite3 import connect

class Database:
    def __init__(self, db_path=":memory:"):
        """Inicializa con la ruta de la base de datos (por defecto en memoria)."""
        self.db_path = db_path

    def create_table(self, df: pd.DataFrame, table_name: str, if_exists="replace"):
        """Crea una tabla en SQLite a partir de un DataFrame."""
        with connect(self.db_path) as conn:
            df.to_sql(table_name, conn, if_exists=if_exists, index=False)
            print(f"✅ Tabla '{table_name}' creada en {self.db_path}")

    def query_table(self, sql: str) -> pd.DataFrame:
        """Ejecuta una consulta y devuelve un DataFrame."""
        with connect(self.db_path) as conn:
            return pd.read_sql(sql, conn)