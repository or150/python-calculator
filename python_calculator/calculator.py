from python_calculator.abstract.evaluation import ExpressionEvaluatorBase
from python_calculator.abstract.syntax import SyntaxParserBase
from python_calculator.abstract.tokens import TokenizerBase
from python_calculator.measurement.call_counter import count_calls


class Calculator:
    def __init__(self, tokenizer: TokenizerBase, syntax_parser: SyntaxParserBase,
                 expression_evaluator: ExpressionEvaluatorBase):
        self._tokenizer = tokenizer
        self._syntax_parser = syntax_parser
        self._expression_evaluator = expression_evaluator

    @count_calls
    def calculate(self, input: str):
        tokens = self._tokenizer.tokenize(input)
        syntax_tree = self._syntax_parser.parse(tokens)
        result = self._expression_evaluator.evaluate(syntax_tree)
        return result
