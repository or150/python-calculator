from dataclasses import dataclass, field

from python_calculator.abstract.tokens import TokenType


@dataclass(frozen=True)
class Token:
    kind: TokenType = field()
    value: str = field()

