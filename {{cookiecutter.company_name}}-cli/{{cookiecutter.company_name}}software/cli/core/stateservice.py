import abc
from typing import Any, Tuple


class StateService(abc.ABC):
    @abc.abstractmethod
    def initialize(self):
        pass

    @abc.abstractmethod
    def cleanup(self):
        pass

    @abc.abstractmethod
    def save_state(self, key: str, value: Any):
        pass

    @abc.abstractmethod
    def remove_state(self, key: str):
        pass

    @abc.abstractmethod
    def load_state(self, key) -> Tuple[str, dict]:
        pass
