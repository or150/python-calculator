from typing import Iterable

from python_calculator.abstract.execution import CalculatorRunnerBase
from python_calculator.calculator import Calculator


class SyncCalculatorRunner(CalculatorRunnerBase):
    def __init__(self, calculator: Calculator):
        self._calculator = calculator

    def calculate_expressions(self, expressions: Iterable[str]) -> Iterable[str]:
        for expression in expressions:
            result = self._calculator.calculate(expression)
            yield result
