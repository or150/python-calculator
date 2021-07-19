from dataclasses import dataclass, field
from typing import Sequence

from python_calculator.abstract.syntax import SyntaxNodeVisitor
from python_calculator.abstract.syntax.nodes import SyntaxNode


@dataclass
class FunctionSyntaxNode(SyntaxNode):
    function: str = field()
    args: Sequence[SyntaxNode] = field()

    def accept(self, visitor: SyntaxNodeVisitor):
        return visitor.visit_function(self)