from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel


class Geolocation(BaseModel):
    ip_address: str
    country_code: str
    country: str
    city: str
    latitude: Decimal
    longitude: Decimal
    mystery_value: str
