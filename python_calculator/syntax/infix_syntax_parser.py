from typing import List, Sequence

from python_calculator.abstract.syntax import SyntaxParserBase
from python_calculator.abstract.syntax.nodes import SyntaxNode, BinaryOperatorSyntaxNode, UnaryOperatorSyntaxNode, \
    LiteralSyntaxNode
from python_calculator.abstract.tokens import Token, TokenType


class InfixSyntaxParser(SyntaxParserBase):
    """
    Parses the input according to these grammar rules
    Expr -> Term | Term {+Term} | Term {-Term}
    Term -> Factor | Factor {* Factor} | Factor {/ Factor}
    Factor -> Base | Base ^ Factor
    Base -> Literal | -Literal
    Literal -> number | (Expr)
    """

    def parse(self, tokens: List[Token]) -> SyntaxNode:
        tokens = list(tokens)
        root_node = self._parse_expr(tokens)
        if tokens:
            raise Exception(f'Invalid input! Got excess tokens after parsing: {tokens}')
        return root_node

    def _parse_expr(self, tokens: List[Token]) -> SyntaxNode:
        terms = []
        operators = []
        while tokens:
            term = self._parse_term(tokens)
            terms.append(term)
            if not tokens or tokens[0].kind != TokenType.Symbol or tokens[0].value not in ('+', '-'):
                break
            operators.append(tokens.pop(0))

        node = terms.pop(0)
        while terms:
            rhs = terms.pop(0)
            operator = operators.pop(0)
            node = BinaryOperatorSyntaxNode(operator=operator.value, lhs=node, rhs=rhs)
        return node

    def _parse_term(self, tokens: List[Token]) -> SyntaxNode:
        terms = []
        operators = []
        while tokens:
            term = self._parse_factor(tokens)
            terms.append(term)
            if not tokens or tokens[0].kind != TokenType.Symbol or tokens[0].value not in ('*', '/'):
                break
            operators.append(tokens.pop(0))

        node = terms.pop(0)
        while terms:
            rhs = terms.pop(0)
            operator = operators.pop(0)
            node = BinaryOperatorSyntaxNode(operator=operator.value, lhs=node, rhs=rhs)

        return node

    def _parse_factor(self, tokens: List[Token]) -> SyntaxNode:
        lhs = self._parse_base(tokens)
        if not tokens:
            return lhs
        if tokens[0].kind != TokenType.Symbol or tokens[0].value != '^':
            return lhs
        token = tokens.pop(0)
        rhs = self._parse_factor(tokens)
        return BinaryOperatorSyntaxNode(operator=token.value, lhs=lhs, rhs=rhs)

    def _parse_base(self, tokens: List[Token]) -> SyntaxNode:
        if tokens[0].kind == TokenType.Symbol and tokens[0].value == '-':
            token = tokens.pop(0)
            literal = self._parse_literal(tokens)
            return UnaryOperatorSyntaxNode(operator=token.value, operand=literal)
        return self._parse_literal(tokens)

    def _parse_literal(self, tokens: List[Token]) -> SyntaxNode:
        if tokens[0].kind == TokenType.Number:
            return LiteralSyntaxNode(value=tokens.pop(0).value)
        elif tokens[0].kind == TokenType.Symbol and tokens[0].value == '(':
            tokens.pop(0)
            expr = self._parse_expr(tokens)

            token = tokens.pop(0)
            if token.kind == TokenType.Symbol and token.value == ')':
                return expr
            else:
                raise Exception(f'Unexpected token: {token}')

        raise Exception(f'Unexpected token: {tokens[0]}')