from typing import Iterable

from python_calculator.abstract.input.input_reader_base import InputReaderBase


class InteractiveInputReader(InputReaderBase):
    def read_input(self) -> Iterable[str]:
        print('Please enter your expression:')
        expression = input()
        return [expression]
