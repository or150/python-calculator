from math import cos

from python_calculator.abstract.evaluation import FunctionHandlerBase


class CosHandler(FunctionHandlerBase):
    @property
    def name(self) -> str:
        return 'cos'

    @property
    def arg_count(self) -> int:
        return 1

    def evaluate(self, *args):
        return cos(args[0])
