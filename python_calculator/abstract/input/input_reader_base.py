from abc import ABC, abstractmethod


class InputReaderBase(ABC):
    @abstractmethod
    def read_input(self) -> str:
        pass
