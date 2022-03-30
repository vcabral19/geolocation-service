import time
from math import trunc

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.data_library.schema_geolocation import GeolocationModel
from app.middleware.app_logger import logger
from app.sql_app.crud import get_geolocation_by_ip
from app.sql_app.database import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return "OK"


@app.get("/geolocation/{ip_address}", response_model=GeolocationModel)
def read_geolocation(ip_address: str, db: Session = Depends(get_db)):
    logger.info(
        f"Processing request for geolocation data for the IP Address: {ip_address}"
    )
    start_time = time.time()
    db_geolocation = get_geolocation_by_ip(db, ip_address)
    if not db_geolocation:
        raise HTTPException(status_code=404, detail="IP Address not found")
    end_time = time.time()
    logger.info(f"Request processing time {trunc((end_time - start_time) * 1000)}ms")
    return db_geolocation
