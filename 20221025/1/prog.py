from itertools import islice
import sys
def fib_gen():
    a, b = 1, 1
    yield a
    while True:
        a, b = b, a + b
        yield a


def fib(m, n):
    yield from islice(fib_gen(), m, m + n)


exec(sys.stdin.read())

