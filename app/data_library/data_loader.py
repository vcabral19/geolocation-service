from pathlib import Path

from app.model_geolocation import GeolocationModel
from app.data_library.csv_parser import csv_handler

CSV_PATH = Path("app").parent / "data/dummy.csv"

if __name__ == "__main__":
    rows = csv_handler(CSV_PATH)
    print(rows)
