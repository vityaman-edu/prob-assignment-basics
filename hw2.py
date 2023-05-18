'''
Probability Theory Homework 2.
Basics.
Variant 16.
Smirnov @vityaman Victor 2023.
'''

from stati import *
from ploti import *

print('Probability Homework 2 by Smirnov Victor')

data = [
    0.76, 0.82, 0.70, 0.86, 0.78, 0.96, 0.68, 0.83, 0.92, 0.86,
    0.86, 0.84, 0.66, 0.92, 0.76, 0.95, 0.84, 1.91, 0.78, 0.70,
    0.78, 0.70, 0.82, 0.99, 0.83, 0.86, 0.67, 0.91, 0.75, 0.86,
    0.83, 0.75, 0.95, 0.79, 0.65, 0.84, 0.78, 0.88, 0.70, 0.95,
    0.87, 0.71, 0.92, 1.00, 0.75, 0.87, 0.80, 0.79, 0.66, 0.90,
    0.79, 0.82, 0.65, 0.83, 0.88, 0.96, 0.75, 0.91, 0.71, 0.87,
    0.76, 0.90, 0.71, 0.87, 0.74, 0.94, 0.80, 1.00, 0.95, 0.79,
    0.96, 0.98, 0.84, 0.79, 0.91, 0.71, 0.65, 0.90, 0.88, 0.74,
    0.74, 0.67, 0.94, 0.72, 1.01, 0.82, 0.80, 0.83, 0.99, 0.83,
    0.88, 0.80, 0.72, 0.91, 0.84, 0.74, 0.94, 0.72, 0.83, 0.87,
]

print('Input data:')
print(data)

data = sorted(data)
print('Sorted data:')
print(data)

distinct_data = sorted(distinct(data))
print('Distinct data:')
print(distinct_data)

print(f'Data size:          {len(data)}')
print(f'Distinct data size: {len(distinct_data)}')

print(f'Max:                {max(data)}')
print(f'Min:                {min(data)}')
print(f'Amplitude:          {amplitude(data)}')
print(f'Mean:               {mean(data)}')
print(f'Variance:           {variance(data)}')
print(f'Standart deviation: {std(data)}')

F = empirical_distribution_function(data)
plot = Plot('Empirical Distribution Function')
plot.function(tabulate(scope(data), 1000), F)
plot.show()

M = 9
h = amplitude(data) / M
hist = histogram(data, h)
plot = Plot('Histogram')
plot.histogram(hist)
plot.points([Point(bin.interval.middle, bin.count) for bin in hist.bin_list])
plot.show()

input('Press any button to exit...')
