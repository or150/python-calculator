from abc import ABC, abstractmethod
from typing import List

from python_calculator.abstract.tokens import Token


class TokenizerBase(ABC):
    @abstractmethod
    def tokenize(self, input: str) -> List[Token]:
        pass
