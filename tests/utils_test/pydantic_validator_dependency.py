from typing import Dict, Type

from pydantic import BaseModel, ValidationError


def pydantic_validator_test(data: Dict, model: Type[BaseModel]) -> bool:
    try:
        model(**data)
    except ValidationError as e:
        return False
    return True
