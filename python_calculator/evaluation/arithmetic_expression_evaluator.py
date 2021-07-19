from typing import List, Dict

from python_calculator.abstract.evaluation import ExpressionEvaluatorBase, FunctionHandlerBase
from python_calculator.abstract.syntax import SyntaxNodeVisitor
from python_calculator.abstract.syntax.nodes import SyntaxNode, BinaryOperatorSyntaxNode, UnaryOperatorSyntaxNode, \
    LiteralSyntaxNode, FunctionSyntaxNode


class ArithmeticSyntaxNodeVisitor(SyntaxNodeVisitor):
    def __init__(self, function_handlers: Dict[str, FunctionHandlerBase]):
        self._function_handlers = function_handlers

    def visit_binary_operator(self, node: BinaryOperatorSyntaxNode):
        operator = node.operator
        lhs = node.lhs.accept(self)
        rhs = node.rhs.accept(self)
        if operator == '+':
            return lhs + rhs
        elif operator == '-':
            return lhs - rhs
        elif operator == '*':
            return lhs * rhs
        elif operator == '/':
            return lhs / rhs
        elif operator == '^':
            return pow(lhs, rhs)
        else:
            raise Exception(f'Unknown binary operator: {operator}')

    def visit_unary_operator(self, node: UnaryOperatorSyntaxNode):
        operator = node.operator
        operand = node.operand.accept(self)
        if operator == '-':
            return -operand
        else:
            raise Exception(f'Unknown unary operator: {operator}')

    def visit_literal(self, node: LiteralSyntaxNode):
        literal = node.value
        return float(literal)

    def visit_function(self, node: FunctionSyntaxNode):
        function = node.function
        args = [arg.accept(self) for arg in node.args]
        handler = self._function_handlers[function]
        if len(args) != handler.arg_count:
            raise Exception(f'"{handler.name}" expects {handler.arg_count} args, got {len(args)}!')
        return handler.evaluate(*args)


class ArithmeticExpressionEvaluator(ExpressionEvaluatorBase):
    def __init__(self, function_handlers: List[FunctionHandlerBase]):
        self._function_handlers = {h.name: h for h in function_handlers}

    def evaluate(self, expression: SyntaxNode):
        visitor = ArithmeticSyntaxNodeVisitor(self._function_handlers)
        result = expression.accept(visitor)
        return result
