import json
import sqlite3
from typing import Tuple, Any

from {{cookiecutter.company_name}}software.cli.core.stateservice import StateService


class SqlLiteStateService(StateService):
    def __init__(self):
        self.conn = sqlite3.connect("{cookiecutter.cli_executable_name}-cli.db")

    def initialize(self):
        try:
            self.conn.execute(
                "CREATE TABLE STATE (KEY CHAR(256) PRIMARY KEY NOT NULL, VALUE TEXT);"
            )
        except sqlite3.OperationalError as oe:
            if oe.args[0] != "table STATE already exists":
                raise

    def cleanup(self):
        self.conn.close()

    def save_state(self, key: str, value: Any):
        value_json = json.dumps(value)
        self.conn.execute(
            "INSERT INTO STATE (KEY, VALUE) VALUES (?, ?)", (key, value_json)
        )
        self.conn.commit()

    def remove_state(self, key: str):
        self.conn.execute("DELETE FROM STATE WHERE KEY = ?", (key,))
        self.conn.commit()

    def load_state(self, key) -> Tuple[str, dict]:
        cursor = self.conn.execute("SELECT KEY, VALUE FROM STATE WHERE KEY = ?", (key,))
        result = cursor.fetchone()
        value_json = json.loads(result[1])
        return result[0], value_json
        return result[0], value_json
