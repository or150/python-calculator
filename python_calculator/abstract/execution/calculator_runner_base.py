from abc import ABC, abstractmethod
from collections import Iterable


class CalculatorRunnerBase(ABC):
    @abstractmethod
    def calculate_expressions(self, expressions: Iterable[str]) -> Iterable[str]:
        pass
