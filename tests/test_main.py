from fastapi.testclient import TestClient

import tests.utils_test.sqlite_dependency as test_sql_dependency
from app.main import app, get_db

app.dependency_overrides[get_db] = test_sql_dependency.override_get_db
client = TestClient(app)


def test_root_endpoint():
    r = client.get("/")
    assert r.status_code == 200


def test_read_geolocation_not_found():

    r = client.get("/geolocation/36.17.140.60")
    assert r.status_code == 404, r.text
    assert r.json()["detail"] == "IP Address not found"


def test_read_geolocation_valid_return():

    expected_payload = {
        "city": "DuBuquemouth",
        "country": "Nepal",
        "country_code": "SI",
        "ip_address": "200.106.141.15",
        "latitude": -84.8750309,
        "longitude": 7.2064359,
        "mystery_value": "7823011346",
    }

    r = client.get("/geolocation/200.106.141.15")
    assert r.status_code == 200, r.text
    assert r.json() == expected_payload
