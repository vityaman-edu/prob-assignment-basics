'''
Statistics functions.
'''

from typing import (
    Collection,
    Iterable,
    List,
    NamedTuple,
    Callable,
)
from numbers import Number
from functools import reduce
from math import sqrt, log, ceil, factorial, exp

Probability = Number

Function = Callable[[Number], Number]


class Interval(NamedTuple):
    begin: Number
    end: Number

    @property
    def length(self) -> Number:
        return self.end - self.begin

    @property
    def middle(self) -> Number:
        return self.begin + self.length / 2
    
    def __str__(self) -> str:
        return f'({self.begin}, {self.end})'


class Bin(NamedTuple):
    interval: Interval
    count: int


class Histogram:
    def __init__(self, bins: List[Bin]):
        self.bin_list = bins

    @property
    def bins(self) -> List[Number]:
        return [self.bin_list[0].interval.begin] + \
            list(map(lambda b: b.interval.end, self.bin_list))

    @property
    def counts(self) -> List[int]:
        return list(map(lambda b: b.count, self.bin_list))


def max(numbers: Collection[Number]) -> Number:
    return reduce(
        lambda a, b: a if a > b else b,
        numbers,
        float('-inf'),
    )


def min(numbers: Collection[Number]) -> Number:
    return reduce(
        lambda a, b: a if a < b else b,
        numbers,
        float('inf'),
    )


def scope(numbers: Collection[Number]) -> Interval:
    return Interval(min(numbers), max(numbers))


def amplitude(numbers: Collection[Number]) -> Number:
    return scope(numbers).length


def mean(numbers: Collection[Number]) -> Number:
    return reduce(
        lambda a, b: a + b,
        numbers,
        0,
    ) / len(numbers)


def variance(numbers: Collection[Number], fixed=False) -> Number:
    m = mean(numbers)
    return reduce(
        lambda a, b: a + (b - m) ** 2,
        numbers,
        0,
    ) / (len(numbers) - (1 if fixed else 0))


def std(numbers: Collection[Number], fixed=False) -> Number:
    return sqrt(variance(numbers, fixed))


def distinct(numbers: Collection[Number]) -> Collection[Number]:
    return set(numbers)


def empirical_distribution_function(numbers: Collection[Number]) -> Function:
    return lambda t: len(list(filter(lambda n: n <= t, numbers))) / len(numbers)


def partition(scope: Interval, n: int) -> Iterable[Interval]:
    step = scope.length / n
    current = scope.begin + step
    while current < scope.end:
        yield Interval(current - step, current)
        current += step


def tabulate(scope: Interval, n: int) -> Iterable[Number]:
    return map(lambda interval: interval.middle, partition(scope, n))


def sturges_step(numbers: Collection[Number]) -> Number:
    return (max(numbers) - min(numbers)) / (1 + log(len(numbers)))


def histogram(numbers: Collection[Number], step) -> Histogram:
    def generate():
        F = empirical_distribution_function(numbers)
        scope = Interval(min(numbers) - step / 2, max(numbers))
        bins = ceil(scope.length / step)
        for interval in partition(scope, bins):
            count = (F(interval.end) - F(interval.begin)) * len(numbers)
            yield Bin(interval, count)
    return Histogram(list(generate()))
