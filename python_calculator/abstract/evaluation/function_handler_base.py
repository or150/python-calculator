from abc import ABC, abstractmethod


class FunctionHandlerBase(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def arg_count(self) -> int:
        pass

    @abstractmethod
    def evaluate(self, *args):
        pass
