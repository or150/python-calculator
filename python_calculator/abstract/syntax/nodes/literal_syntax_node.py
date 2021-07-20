from dataclasses import dataclass, field

from python_calculator.abstract.syntax import SyntaxNodeVisitor
from python_calculator.abstract.syntax.nodes import SyntaxNode


@dataclass
class LiteralSyntaxNode(SyntaxNode):
    value: str = field()

    def accept(self, visitor: SyntaxNodeVisitor):
        return visitor.visit_literal(self)
