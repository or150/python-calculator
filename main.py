from argparse import ArgumentParser
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor

from python_calculator.calculator import Calculator
from python_calculator.evaluation.arithmetic_expression_evaluator import ArithmeticExpressionEvaluator
from python_calculator.evaluation.boolean_expression_evaluator import BooleanExpressionEvaluator
from python_calculator.evaluation.cos_handler import CosHandler
from python_calculator.evaluation.pi_handler import PiHandler
from python_calculator.evaluation.root_handler import RootHandler
from python_calculator.evaluation.sin_handler import SinHandler
from python_calculator.evaluation.sqrt_handler import SqrtHandler
from python_calculator.execution import SyncCalculatorRunner, ParallelCalculatorRunner
from python_calculator.input import InputReaderFactory
from python_calculator.measurement.execution_time_counter import ExecutionTimeCounter
from python_calculator.measurement.progress_counter import ProgressCounter
from python_calculator.syntax.infix_syntax_parser import InfixSyntaxParser
from python_calculator.syntax.polish_notation_syntax_parser import PolishNotationSyntaxParser
from python_calculator.tokens.tokenizer import Tokenizer


def main():
    parser = _create_arg_parser()
    args = parser.parse_args()

    function_handlers = [
        SinHandler(),
        CosHandler(),
        PiHandler(),
        SqrtHandler(),
        RootHandler()
    ]
    infix_parser = InfixSyntaxParser()
    polish_parser = PolishNotationSyntaxParser(function_handlers)
    arithmetic_evaluator = ArithmeticExpressionEvaluator(function_handlers)
    boolean_evaluator = BooleanExpressionEvaluator()
    calculator = Calculator(
        tokenizer=Tokenizer(),
        syntax_parser=infix_parser,
        expression_evaluator=arithmetic_evaluator
    )
    input_reader_factory = InputReaderFactory()
    input_reader = input_reader_factory.create_reader(args.file)
    execution_time_counter = ExecutionTimeCounter()
    progress_counter = ProgressCounter()
    runner = _create_calculator_runner(args, calculator)

    expressions = input_reader.read_input()
    progress_counter.start()
    with execution_time_counter.measure():
        results = []
        for result in runner.calculate_expressions(expressions):
            results.append(result)
            progress_counter.increment_call_count()

    progress_counter.stop()
    for result in results:
        print(result)
    print(f'Call count: {progress_counter.call_count}')
    print(f'Total execution time: {execution_time_counter.total_execution_time}')
    print(f'Average execution time: {execution_time_counter.total_execution_time / progress_counter.call_count}')


def _create_arg_parser():
    parser = ArgumentParser()
    parser.add_argument('--file', '-f', default=None, required=False)
    execution_group = parser.add_mutually_exclusive_group()
    execution_group.add_argument('--sync', '-s', dest='runner', action='store_const', const='sync')
    execution_group.add_argument('--multiprocess', '-p', dest='runner', action='store_const', const='multiprocess')
    execution_group.add_argument('--multithreaded', '-t', dest='runner', action='store_const', const='threading')
    execution_group.set_defaults(runner='multiprocess')
    parser.add_argument('--batch_size', '-b', default=100, required=False, type=int)
    parser.add_argument('--num_workers', '-n', default=5, required=False, type=int)
    return parser


def _create_calculator_runner(args, calculator):
    if args.runner == 'sync':
        runner = SyncCalculatorRunner(calculator)
    elif args.runner in ('multiprocess', 'threading'):
        if args.runner == 'multiprocess':
            executor = ProcessPoolExecutor(max_workers=args.num_workers)
        else:
            executor = ThreadPoolExecutor(max_workers=args.num_workers)
        runner = ParallelCalculatorRunner(
            calculator=calculator,
            executor=executor,
            batch_size=args.batch_size
        )
    else:
        raise Exception(f'Unknown runner type: {args.runner}!')
    return runner


if __name__ == '__main__':
    main()
