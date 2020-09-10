import abc
from typing import Any, Tuple


class KeyValueStore(abc.ABC):
    @abc.abstractmethod
    def initialize(self):
        pass

    @abc.abstractmethod
    def cleanup(self):
        pass

    def __del__(self):
        pass

    @abc.abstractmethod
    def set(self, key: str, value: Any):
        pass

    @abc.abstractmethod
    def remove(self, key: str):
        pass

    @abc.abstractmethod
    def get(self, key) -> Tuple[str, dict]:
        pass
