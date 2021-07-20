import typing
from abc import ABC, abstractmethod

if typing.TYPE_CHECKING:
    from python_calculator.abstract.syntax.nodes import LiteralSyntaxNode, BinaryOperatorSyntaxNode, \
        UnaryOperatorSyntaxNode


class SyntaxNodeVisitor(ABC):
    @abstractmethod
    def visit_binary_operator(self, node: 'BinaryOperatorSyntaxNode'):
        pass

    @abstractmethod
    def visit_unary_operator(self, node: 'UnaryOperatorSyntaxNode'):
        pass

    @abstractmethod
    def visit_literal(self, node: 'LiteralSyntaxNode'):
        pass
