import functools


def count_calls(func):
    @functools.wraps(func)
    def call(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        finally:
            call.call_count += 1

    call.call_count = 0
    return call
