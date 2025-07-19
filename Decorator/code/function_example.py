"""
Пример показывает как добавление декоратора позволяет ускорить работу программы
"""


import sys


def memoize(f):
    cache = dict()

    def wrapper(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]

    return wrapper


@memoize
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    print(fib(750))
