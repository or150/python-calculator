from python_calculator.abstract.evaluation import ExpressionEvaluatorBase
from python_calculator.abstract.syntax import SyntaxNodeVisitor
from python_calculator.abstract.syntax.nodes import SyntaxNode, BinaryOperatorSyntaxNode, UnaryOperatorSyntaxNode, \
    LiteralSyntaxNode


class ArithmeticSyntaxNodeVisitor(SyntaxNodeVisitor):
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


class ArithmeticExpressionEvaluator(ExpressionEvaluatorBase):
    def evaluate(self, expression: SyntaxNode):
        visitor = ArithmeticSyntaxNodeVisitor()
        result = expression.accept(visitor)
        return result
