from abc import ABC, abstractmethod

from python_calculator.abstract.syntax.nodes import SyntaxNode


class ExpressionEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, expression: SyntaxNode):
        pass
