from math import sqrt

from python_calculator.abstract.evaluation import FunctionHandlerBase


class SqrtHandler(FunctionHandlerBase):
    @property
    def name(self) -> str:
        return 'sqrt'

    @property
    def arg_count(self) -> int:
        return 1

    def evaluate(self, *args):
        return sqrt(args[0])
