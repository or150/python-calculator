from abc import ABC, abstractmethod
from typing import List

from python_calculator.abstract.syntax.nodes import SyntaxNode
from python_calculator.abstract.tokens import Token


class SyntaxParserBase(ABC):
    @abstractmethod
    def parse(self, tokens: List[Token]) -> SyntaxNode:
        pass
