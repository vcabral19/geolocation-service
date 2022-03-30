from pathlib import Path

from app.config import get_variable
from app.data_library.csv_parser import csv_handler
from app.sql_app.crud import create_geolocations
from app.sql_app.database import SessionLocal

CSV_PATH = Path(get_variable("CSV_PATH"))
REPORT_BY_LINE = eval(get_variable("REPORT_BY_LINE"))

if __name__ == "__main__":
    session = SessionLocal()
    rows = csv_handler(CSV_PATH, REPORT_BY_LINE)
    create_geolocations(session, rows)
