from typing import Iterable

from python_calculator.abstract.input.input_reader_base import InputReaderBase


class FileInputReader(InputReaderBase):
    def __init__(self, file_name: str):
        self._file_name = file_name

    def read_input(self) -> Iterable[str]:
        with open(self._file_name, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    yield line
