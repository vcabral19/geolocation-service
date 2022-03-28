import csv

from pathlib import Path
from typing import Type, List, Mapping

from pydantic import BaseModel, parse_file_as


def csv_to_object(filepath: Path):
    rows = []
    with open(filepath, "r") as file:
        reader = csv.reader(file)

        fields = next(reader)

        for row in reader:
            rows.append(row)
    return fields, rows


def data_validation(model: Type[BaseModel], filepath: Path):
    objects = parse_file_as(List[model], filepath)
    return objects
