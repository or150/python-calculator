import functools
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor
from typing import Iterable, Union, List

from python_calculator.abstract.execution import CalculatorRunnerBase
from python_calculator.calculator import Calculator


class ParallelCalculatorRunner(CalculatorRunnerBase):
    def __init__(self, calculator: Calculator, executor: Union[ThreadPoolExecutor, ProcessPoolExecutor],
                 batch_size: int):
        self._calculator = calculator
        self._executor = executor
        self._batch_size = batch_size

    def calculate_expressions(self, expressions: Iterable[str]) -> Iterable[str]:
        expression_batches = batch_iterable(expressions, self._batch_size)
        calculate_batch_method = functools.partial(_calculate_batch, self._calculator)
        for results_batch in self._executor.map(calculate_batch_method, expression_batches):
            for result in results_batch:
                yield result


def _calculate_batch(calculator: Calculator, batch: List[str]) -> List[str]:
    return [calculator.calculate(expression) for expression in batch]


def batch_iterable(iterable: Iterable, size: int) -> Iterable[list]:
    input_iterator = iter(iterable)
    while True:
        batch = []
        try:
            for _ in range(size):
                batch.append(next(input_iterator))
        except StopIteration:
            break
        finally:
            if batch:
                yield batch
