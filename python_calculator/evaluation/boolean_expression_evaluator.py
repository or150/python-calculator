from python_calculator.abstract.evaluation import ExpressionEvaluatorBase
from python_calculator.abstract.syntax import SyntaxNodeVisitor
from python_calculator.abstract.syntax.nodes import SyntaxNode, BinaryOperatorSyntaxNode, UnaryOperatorSyntaxNode, \
    LiteralSyntaxNode, FunctionSyntaxNode


class BooleanSyntaxNodeVisitor(SyntaxNodeVisitor):
    def visit_binary_operator(self, node: BinaryOperatorSyntaxNode):
        operator = node.operator
        lhs = node.lhs.accept(self)
        rhs = node.rhs.accept(self)
        if operator == '+':
            return int(lhs or rhs)
        elif operator == '*':
            return int(lhs and rhs)
        else:
            raise Exception(f'Unsupported binary operator: {operator}')

    def visit_unary_operator(self, node: UnaryOperatorSyntaxNode):
        operator = node.operator
        operand = node.operand.accept(self)
        if operator == '~':
            if operand:
                return 0
            return 1
        else:
            raise Exception(f'Unsupported unary operator: {operator}')

    def visit_literal(self, node: LiteralSyntaxNode):
        literal = node.value
        value = int(literal)
        if value not in (0,1):
            raise Exception(f'Unsupported literal: {literal}')
        return value

    def visit_function(self, node: FunctionSyntaxNode):
        raise Exception('Functions are not supported in boolean algebra mode')


class BooleanExpressionEvaluator(ExpressionEvaluatorBase):
    def evaluate(self, expression: SyntaxNode):
        visitor = BooleanSyntaxNodeVisitor()
        result = expression.accept(visitor)
        return result
