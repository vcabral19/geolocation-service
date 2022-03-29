import csv
from pathlib import Path
from typing import Dict, List

import pydantic

from app.data_library.csv_parser import _csv_to_object, csv_handler

BROKEN_SCHEMA_DATA = "tests/resources/broken_schema_data.csv"
INVALID_DATA = "tests/resources/test_invalid_data.csv"
VALID_DATA = "tests/resources/test_valid_data.csv"


def check_type(obj, expected_type):
    class Model(pydantic.BaseModel):
        data: expected_type

    try:
        Model(data=obj)
    except pydantic.ValidationError as ve:
        raise TypeError(str(ve.errors()))

    return True


class TestParser:
    def test_csv_handler_contract(self):
        assert check_type(csv_handler(Path(VALID_DATA)), List[Dict[str, str]])

    def test_csv_to_object_valid_data(self):
        with open(VALID_DATA, "r") as file:
            reader = csv.reader(file)
            result = _csv_to_object(reader)

        assert len(result) == 4

    def test_csv_to_object_invalid_data(self):
        with open(INVALID_DATA, "r") as file:
            reader = csv.reader(file)
            result = _csv_to_object(reader)

        assert len(result) == 1
