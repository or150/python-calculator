import functools
import random


def generate_expression(max_depth: int = 4) -> str:
    def binary_op(operator):
        lhs = generate_expression(max_depth - 1)
        rhs = generate_expression(max_depth - 1)
        return f'({lhs}{operator}{rhs})'

    multiply = functools.partial(binary_op, '*')
    add = functools.partial(binary_op, '+')
    power = functools.partial(binary_op, '^')

    def power():
        lhs = generate_expression(max_depth - 1)
        rhs = value()
        return f'({lhs}^{rhs})'

    def value():
        number = random.uniform(1, 3)
        return format(number, '0.2f')

    if max_depth == 0:
        return value()
    method = random.choice([multiply, value, add, power])
    return method()


def main():
    with open('input.txt', 'w') as f:
        for _ in range(100000):
            f.write(generate_expression() + '\n')


if __name__ == '__main__':
    main()
