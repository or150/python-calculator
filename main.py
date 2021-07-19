from argparse import ArgumentParser

from python_calculator.calculator import Calculator
from python_calculator.evaluation.arithmetic_expression_evaluator import ArithmeticExpressionEvaluator
from python_calculator.input import InputReaderFactory
from python_calculator.measurement.execution_time_counter import ExecutionTimeCounter
from python_calculator.measurement.progress_counter import ProgressCounter
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
    expressions = input_reader.read_input()
    counter = ExecutionTimeCounter()

    progress_counter = ProgressCounter(calculator)
    progress_counter.start()
    results = []
    for expression in expressions:
        with counter.measure():
            result = calculator.calculate(expression)
        results.append(result)
    progress_counter.stop()
    for result in results:
        print(result)
    print(f'Call count: {calculator.calculate.call_count}')
    print(f'Total execution time: {counter.total_execution_time}')
    print(f'Average execution time: {counter.average_execution_time}')


if __name__ == '__main__':
    main()
