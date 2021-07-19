from argparse import ArgumentParser

from python_calculator.calculator import Calculator
from python_calculator.evaluation.arithmetic_expression_evaluator import ArithmeticExpressionEvaluator
from python_calculator.input import InputReaderFactory
from python_calculator.syntax.infix_syntax_parser import InfixSyntaxParser
from python_calculator.tokens.tokenizer import Tokenizer


def main():
    parser = ArgumentParser()
    parser.add_argument('--file', '-f', metavar='file', default=None, required=False)
    args = parser.parse_args()

    calculator = Calculator(
        tokenizer=Tokenizer(),
        syntax_parser=InfixSyntaxParser(),
        expression_evaluator=ArithmeticExpressionEvaluator()
    )
    input_reader_factory = InputReaderFactory()
    input_reader = input_reader_factory.create_reader(args.file)
    expression = input_reader.read_input()
    result = calculator.calculate(expression)
    print(result)
    print(f'Call count: {calculator.calculate.call_count}')


if __name__ == '__main__':
    main()
