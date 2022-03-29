from pydantic import BaseModel, condecimal, constr


class GeolocationModel(BaseModel):
    ip_address: constr(
        regex=r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
    )
    country_code: constr(min_length=1, max_length=5)
    country: constr(min_length=2, max_length=50)
    city: constr(min_length=2, max_length=100)
    latitude: condecimal(gt=-90, lt=90)
    longitude: condecimal(gt=-180, lt=180)
    mystery_value: str

    class Config:
        orm_mode = True

