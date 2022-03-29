from pathlib import Path

from app.config import get_variable
from app.data_library.csv_parser import csv_handler

CSV_PATH = Path(get_variable("CSV_PATH"))
REPORT_BY_LINE = get_variable("REPORT_BY_LINE", bool)

if __name__ == "__main__":
    rows = csv_handler(CSV_PATH, REPORT_BY_LINE)
