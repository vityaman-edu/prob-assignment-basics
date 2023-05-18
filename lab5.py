'''
Probability Theory Assignment 1.
Basics.
Variant 16.
Smirnov @vityaman Victor 2023.
(1, 16) - (1, 20), (2, 16) - (2, 20)
'''

from stati import *
from ploti import *

print('Probability Theory Assignment 1 by Smirnov Victor')

numbers = [
    -0.45, 0.52, -1.63, -0.42, -1.18,
    1.42,  0.66, -1.70,  0.17,  0.14,
    0.83, -0.48, -1.35,  0.31,  0.59,
    0.73,  0.00,  1.59,  0.17, -0.45
]

print('Input data:')
print(numbers)

numbers = sorted(numbers)
print('Sorted data:')
print(numbers)

distinct_numbers = sorted(distinct(numbers))
print('Distinct data:')
print(distinct_numbers)

print(f'Data size:          {len(numbers)}')
print(f'Distinct data size: {len(distinct_numbers)}')

print(f'Max:                {max(numbers)}')
print(f'Min:                {min(numbers)}')
print(f'Amplitude:          {amplitude(numbers)}')
print(f'Mean:               {mean(numbers)}')
print(f'Variance:           {variance(numbers, fixed=True)}')
print(f'Standart deviation: {std(numbers, fixed=True)}')


F = empirical_distribution_function(numbers)
print('Empirical Distribution Function')
for number in numbers:
    print(f'F(x <= {number}) = {F(number)}')

plot = Plot('Empirical Distribution Function')
plot.function(tabulate(scope(numbers), 1000), F)
plot.show()

hist = histogram(numbers, sturges_step(numbers))
print('Histogram')
print('interval', 'count', sep='\t')
for bin in hist.bin_list:
    print(f'{bin.interval}\t{round(bin.count)}')

plot = Plot('Histogram')
plot.histogram(hist)
plot.points([Point(bin.interval.middle, bin.count) for bin in hist.bin_list])
plot.show()

input('Press any button to exit...')
