from dataclasses import dataclass, field

from python_calculator.abstract.syntax import SyntaxNodeVisitor
from python_calculator.abstract.syntax.nodes import SyntaxNode


@dataclass
class UnaryOperatorSyntaxNode(SyntaxNode):
    operator: str = field()
    operand: SyntaxNode = field()

    def accept(self, visitor: SyntaxNodeVisitor):
        return visitor.visit_unary_operator(self)