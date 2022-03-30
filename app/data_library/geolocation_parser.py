import csv
from pathlib import Path
from typing import Dict, List, Type

from pydantic import BaseModel, ValidationError

from app.data_library.schema_geolocation import GeolocationModel
from app.middleware.app_logger import logger


def csv_handler(filepath: Path, broken_lines_report: bool = False) -> List[Dict]:

    with open(filepath, "r") as file:
        reader = csv.reader(file)

        parsable_rows = _extraction_pipeline(reader, broken_lines_report)

    return parsable_rows


def _extraction_pipeline(
    csv_reader: csv.reader, broken_lines_report: bool
) -> List[Dict]:
    fields = next(csv_reader)
    buffer = []
    for index, row in enumerate(csv_reader):
        try:
            if len(fields) == len(row):
                dict_row = dict(zip(fields, row))
                _data_validation(dict_row, GeolocationModel)
            else:
                raise FieldsRowsMismatchError
        except Exception as error:
            if broken_lines_report:
                logger.error(
                    f"Ops! line {index} of the .csv being parsed raised {error}"
                )
        else:
            buffer.append(dict_row)
    unique_rows = [
        dict(tuple) for tuple in {tuple(sorted(dict.items())) for dict in buffer}
    ]
    result_len = len(unique_rows)
    logger.info("The csv parsing and sanitization complete!")
    logger.info(f"Total lines processed: {index + 1}")
    logger.info(
        f"Lines accepted: {result_len} - Lines discarded: {index + 1 - result_len}"
    )
    return unique_rows


def _data_validation(data: Dict, model: Type[BaseModel]) -> None:
    try:
        model(**data)
    except ValidationError as e:
        raise e


class FieldsRowsMismatchError(Exception):
    def __str__(self):
        return f"{__class__.__name__}: Number of fields in the Row and expected number of columns on the file does not match"
