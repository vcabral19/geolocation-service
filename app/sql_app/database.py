from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import get_variable

POSTGRES_USER = get_variable("POSTGRES_USER")
POSTGRES_PASSWORD = get_variable("POSTGRES_PASSWORD")
POSTGRES_SERVER = get_variable("POSTGRES_SERVER")
POSTGRES_DB = get_variable("POSTGRES_DB")
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
