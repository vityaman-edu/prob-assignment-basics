'''
Plotting functions.
'''

import matplotlib.pyplot as plt
from typing import NamedTuple, Collection, Callable, List
from numbers import Number
from stati import Histogram

Function = Callable[[Number], Number]


class Point(NamedTuple):
    x: Number
    y: Number


class Plot:
    def __init__(self, title: str = ""):
        self.figure, self.axes = plt.subplots()
        self.axes.set_title(title)

    def points(self, points: Collection[Point]):
        self.axes.plot(
            list(map(lambda p: p.x, points)),
            list(map(lambda p: p.y, points))
        )

    def function(self, x: Collection[Number], f: Function):
        self.points(list(map(lambda x: Point(x, f(x)), x)))

    def histogram(self, histogram: Histogram):
        bins = histogram.bins
        counts = histogram.counts
        self.axes.hist(bins[:-1], bins, weights=counts)

    def show(self):
        plt.ion()
        plt.show()
