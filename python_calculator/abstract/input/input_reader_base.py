from abc import ABC, abstractmethod
from typing import Iterable


class InputReaderBase(ABC):
    @abstractmethod
    def read_input(self) -> Iterable[str]:
        pass
