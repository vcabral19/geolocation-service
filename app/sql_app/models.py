from sqlalchemy import Column, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base


class GeolocationORM(Base):
    __tablename__ = 'geolocation'
    ip_address = Column(String(20), index=True)
    country_code = Column(String(5))
    city = Column(String(50))
    latitude = Column(DECIMAL(precision=7))
    longitude = Column(DECIMAL(precision=7))
    mystery_value = Column(String(100))
