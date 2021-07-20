from python_calculator.calculator import Calculator
from python_calculator.evaluation.arithmetic_expression_evaluator import ArithmeticExpressionEvaluator
from python_calculator.syntax.infix_syntax_parser import InfixSyntaxParser
from python_calculator.tokens.tokenizer import Tokenizer


def main():
    calculator = Calculator(
        tokenizer=Tokenizer(),
        syntax_parser=InfixSyntaxParser(),
        expression_evaluator=ArithmeticExpressionEvaluator()
    )
    print('Please enter your expression:')
    result = calculator.calculate(input())
    print(result)


if __name__ == '__main__':
    main()
