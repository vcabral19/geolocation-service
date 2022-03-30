from typing import Dict, List

from sqlalchemy.orm import Session

from app.data_library import schema_geolocation
from app.sql_app import models


def get_geolocation_by_ip(db: Session, ip_address: str):
    return (
        db.query(models.GeolocationORM)
        .filter(models.GeolocationORM.ip_address == ip_address)
        .first()
    )


def get_all_geolocation_by_ip(
    db: Session, ip_address: str, skip: int = 0, limit: int = 100
):
    return (
        db.query(models.GeolocationORM)
        .filter(models.GeolocationORM.ip_address == ip_address)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_geolocations(db: Session, geolocation_rows: List[Dict]) -> None:
    db.bulk_insert_mappings(models.GeolocationORM, geolocation_rows)
    db.commit()
