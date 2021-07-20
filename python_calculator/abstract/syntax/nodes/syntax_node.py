from abc import ABC, abstractmethod

from python_calculator.abstract.syntax import SyntaxNodeVisitor


class SyntaxNode(ABC):
    @abstractmethod
    def accept(self, visitor: SyntaxNodeVisitor):
        pass
