from math import pi

from python_calculator.abstract.evaluation import FunctionHandlerBase


class PiHandler(FunctionHandlerBase):
    @property
    def name(self) -> str:
        return 'pi'

    @property
    def arg_count(self) -> int:
        return 0

    def evaluate(self, *args):
        return pi
