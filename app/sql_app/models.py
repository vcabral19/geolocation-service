from sqlalchemy import DECIMAL, Column, String

from app.sql_app.database import Base


class GeolocationORM(Base):
    __tablename__ = "geolocation"
    ip_address = Column(String(16), primary_key=True, index=True)
    country_code = Column(String(5))
    country = Column(String(50))
    city = Column(String(50))
    latitude = Column(DECIMAL(precision=10, scale=7))
    longitude = Column(DECIMAL(precision=10, scale=7))
    mystery_value = Column(String(100))
