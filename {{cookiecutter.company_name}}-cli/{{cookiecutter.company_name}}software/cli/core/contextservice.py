from typing import Any

from {{cookiecutter.company_name}}software.cli.core.keyvaluestore import KeyValueStore
from {{cookiecutter.company_name}}software.cli.core.logger import CliOutput


class ContextService:
    def __init__(self, context_dict: dict):
        self.context_dict = context_dict

    def get_cli_output(self) -> CliOutput:
        return self.context_dict["log"]

    def get_store(self) -> KeyValueStore:
        return self.context_dict["store"]

    def add(self, key, value: Any):
        self.context_dict[key] = value

    def get(self, key) -> Any:
        return self.context_dict[key]
