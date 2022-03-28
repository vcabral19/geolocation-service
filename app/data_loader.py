from pathlib import Path

from model_geolocation import Geolocation
from data_library.csv_parser import csv_to_object

CSV_PATH = Path("/Users/vitorcabral/studies/geolocation-service/data/dummy.csv")

if __name__ == "__main__":
    fields, rows = csv_to_object(CSV_PATH)
    print(fields)
    print(rows)
