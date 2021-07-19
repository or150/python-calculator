from math import sqrt

from python_calculator.abstract.evaluation import FunctionHandlerBase


class RootHandler(FunctionHandlerBase):
    @property
    def name(self) -> str:
        return 'root'

    @property
    def arg_count(self) -> int:
        return 2

    def evaluate(self, *args):
        return pow(args[0], 1/args[1])
