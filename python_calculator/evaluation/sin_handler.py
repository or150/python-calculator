from math import sin

from python_calculator.abstract.evaluation import FunctionHandlerBase


class SinHandler(FunctionHandlerBase):
    @property
    def name(self) -> str:
        return 'sin'

    @property
    def arg_count(self) -> int:
        return 1

    def evaluate(self, *args):
        return sin(args[0])
