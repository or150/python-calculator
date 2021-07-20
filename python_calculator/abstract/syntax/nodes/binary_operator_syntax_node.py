from dataclasses import dataclass, field

from python_calculator.abstract.syntax import SyntaxNodeVisitor
from python_calculator.abstract.syntax.nodes import SyntaxNode


@dataclass
class BinaryOperatorSyntaxNode(SyntaxNode):
    operator: str = field()
    lhs: SyntaxNode = field()
    rhs: SyntaxNode = field()

    def accept(self, visitor: SyntaxNodeVisitor):
        return visitor.visit_binary_operator(self)