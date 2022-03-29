import configparser
import os
from pathlib import Path
from typing import Any


def get_variable(variable_name: str, variable_type: Any = str) -> Any:
    config_var = os.environ.get(variable_name, _get_config(variable_name))
    return variable_type(config_var)


def _get_config(variable_name: str) -> str:
    path_prefix = Path("app") / "config"
    cfg = configparser.ConfigParser()

    app_running_env = os.environ.get("ENVIRONMENT", "dev")
    if app_running_env == "prod":
        file_name = "config_prod.ini"
    elif app_running_env == "staging":
        file_name = "config_prod.ini"
    else:
        file_name = "config_dev.ini"

    cfg.read(path_prefix / file_name)

    return cfg["geolocation_app"][variable_name]
