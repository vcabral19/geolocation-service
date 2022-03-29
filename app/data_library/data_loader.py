from pathlib import Path

from app.data_library.csv_parser import csv_handler
from app.model_geolocation import GeolocationModel

# CSV_PATH = Path("app").parent / "data/dummy.csv"
CSV_PATH = Path("app").parent / "data/data_dump.csv"

if __name__ == "__main__":
    rows = csv_handler(CSV_PATH)
    # print(rows)
