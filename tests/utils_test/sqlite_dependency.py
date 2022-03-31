import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.sql_app.crud import create_geolocations
from app.sql_app.database import Base
from app.sql_app.models import GeolocationORM

DATA_DUMP = "tests/resources/test_data_dump.json"
SQLALCHEMY_DATABASE_URL = "sqlite+pysqlite:///./db.sqlite3:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, bind=engine)

try:
    GeolocationORM.__table__.drop(engine)
except:
    pass


def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=engine)

with open(DATA_DUMP) as json_file:
    rows = json.load(json_file)
    json_file.close()

create_geolocations(next(override_get_db()), rows)
