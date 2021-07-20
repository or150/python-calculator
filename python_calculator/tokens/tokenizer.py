import re
from typing import List

from python_calculator.abstract.tokens import TokenizerBase, Token, TokenType


class Tokenizer(TokenizerBase):
    def tokenize(self, input: str) -> List[Token]:
        tokens = []
        i = 0
        while i < len(input):
            char = input[i]
            if char == ' ':
                i += 1
            elif char in ['(', ')', '+', '-', '/', '*', ',', '^', '!']:
                tokens.append(Token(kind=TokenType.Symbol, value=char))
                i += 1
            elif char.isdigit():
                value = self._get_number(input[i:])
                tokens.append(Token(kind=TokenType.Number, value=value))
                i += len(value)
            elif char.isalpha():
                value = self._get_identifier(input[i:])
                tokens.append(Token(kind=TokenType.Identifier, value=value))
                i += len(value)
            else:
                raise ValueError(f'Unexpected character: {char} at: {i}')
        return tokens

    def _get_number(self, input: str):
        match = re.match(r'\d+(?:\.\d+)?', input)
        return match.group(0)

    def _get_identifier(self, input: str):
        match = re.match(r'[A-Za-z][A-Za-z_\d]*', input)
        return match.group(0)
