from typing import List

from python_calculator.abstract.evaluation import FunctionHandlerBase
from python_calculator.abstract.syntax import SyntaxParserBase
from python_calculator.abstract.syntax.nodes import SyntaxNode, LiteralSyntaxNode, BinaryOperatorSyntaxNode, \
    FunctionSyntaxNode, UnaryOperatorSyntaxNode
from python_calculator.abstract.tokens import Token, TokenType


class PolishNotationSyntaxParser(SyntaxParserBase):
    def __init__(self, function_handlers: List[FunctionHandlerBase]):
        self._function_handlers = {handler.name: handler for handler in function_handlers}

    def parse(self, tokens: List[Token]) -> SyntaxNode:
        tokens = list(tokens)
        root_node = self._parse(tokens)
        if tokens:
            raise Exception(f'Invalid input! Got excess tokens after parsing: {tokens}')
        return root_node

    def _parse(self, tokens: List[Token]) -> SyntaxNode:
        token = tokens.pop(0)
        if token.kind == TokenType.Number:
            return LiteralSyntaxNode(value=token.value)
        elif token.kind == TokenType.Symbol and token.value in ('+', '-', '*', '/', '^'):
            lhs = self._parse(tokens)
            rhs = self._parse(tokens)
            return BinaryOperatorSyntaxNode(operator=token.value, lhs=lhs, rhs=rhs)
        elif token.kind == TokenType.Symbol and token.value == '!':
            operand = self._parse(tokens)
            return UnaryOperatorSyntaxNode(operator=token.value, operand=operand)
        elif token.kind == TokenType.Identifier:
            handler = self._function_handlers[token.value]
            args = []
            for _ in range(handler.arg_count):
                args.append(self._parse(tokens))
            return FunctionSyntaxNode(function=token.value, args=args)
        elif token.kind == TokenType.Symbol and token.value in ('(', ')'):
            raise Exception(f'Brackets are not supported in Polish Notation!')
        else:
            raise Exception(f'Unexpected token: {[token] + tokens}')
