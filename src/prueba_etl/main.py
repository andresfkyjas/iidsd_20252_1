
import pandas as pd
from database import Database
from extractor import Extractor





if __name__ == "__main__":
    # DataFrame de ejemplo
    ruta_db = "/workspaces/iidsd_20252_1/src/prueba_etl/static/db/database.sqlite"
    url = "uom190346a/global-coffee-health-dataset"
    database = Database(ruta_db)
    extractor = Extractor()
    dataset = extractor.download_dataset_zip(url) 
    csv_dir =extractor.extract_zip_files(dataset)
    df = extractor.create_csv(csv_dir)
    print(df.head(2))
    database.create_table(df, "coffee_health")
