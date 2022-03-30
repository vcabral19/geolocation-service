import time
from pathlib import Path

from app.config import get_variable
from app.data_library.geolocation_parser import csv_handler
from app.middleware.app_logger import logger
from app.sql_app.crud import create_geolocations
from app.sql_app.database import SessionLocal

CSV_PATH = Path(get_variable("CSV_PATH"))
REPORT_BY_LINE = eval(get_variable("REPORT_BY_LINE"))

if __name__ == "__main__":
    session = SessionLocal()

    start_time = time.time()

    rows = csv_handler(CSV_PATH, REPORT_BY_LINE)
    parsing_end_time = time.time()
    logger.info(
        f"Parsing process took in total: ------ {parsing_end_time - start_time} seconds ------"
    )

    create_geolocations(session, rows)
    total_end_time = time.time()
    logger.info(
        f"Total data importing process took in total: ------ {total_end_time - start_time} seconds ------"
    )
