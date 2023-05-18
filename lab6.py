'''
Probability Theory Assignment 2.
Basics.
Variant 16.
Smirnov @vityaman Victor 2023.
'''

from stati import *

print('Assigment 6 by Victor Smirnov')
print()


def student(n: int, p: Number) -> Number:
    if n == 9 and p == 0.995:
        return 3.25
    if n == 64 and p == 0.95:
        return 1.671


print('Problem 1.6')

data = sorted([
    0.30, 0.28, 0.27, 0.33, 0.35,
    0.33, 0.27, 0.31, 0.37, 0.29,
])
gamma = 0.99

print(f'Data:  {data}')
print(f'Size:  {len(data)}')
print(f'Gamma: {gamma}')

n = len(data)
m = mean(data)
s = std(data, fixed=True)
t = student(n - 1, (1 + gamma) / 2)
interval = Interval(m - t * s / sqrt(n), m + t * s / sqrt(n))
print(f'N:        {n}')
print(f'mean:     {m}')
print(f'std:      {s}')
print(f't:        {t}')
print(f'Interval: {interval}')
print()

print('Problem 1.6')

n = 64
m = 5452.8 / n
s = sqrt(973.44 / n)
gamma = 0.9
t = student(n, (1 + gamma) / 2)
interval = Interval(m - t * s / sqrt(n), m + t * s / sqrt(n))
print(f'N:        {n}')
print(f'mean:     {m}')
print(f'std:      {s}')
print(f't:        {t}')
print(f'Interval: {interval}')
print()

print('Problem 16')

#      0    1    2   3   4  5  6  7
a = [112, 168, 130, 69, 32, 5, 1, 1]
n = sum(a)
m = sum(i * a[i] for i in range(len(a))) / n
alpha = 0.01

print(f'Data: {a}')
print(f'Size: {n}')
print(f'Mean: {m}')


def puasson(lmbd: Number) -> Callable[[int], Number]:
    return lambda i: lmbd ** i / factorial(i) * exp(-lmbd)


p = puasson(m)

print('Table A')
for i in range(len(a)):
    print(f'{i}\t{a[i]}\t{p(i)}\t{p(i) * n}')


b = [112, 168, 130, 69, 32, 7]
n = sum(b)
m = sum(i * b[i] for i in range(len(b))) / n

p = puasson(m)

print('Table B')
for i in range(len(b)):
    print(f'{i}\t{b[i]}\t{p(i)}\t{p(i) * n}')

actual_chi2 = sum(
    (b[i] - p(i) * n) ** 2 / (p(i) * n) \
        for i in range(len(b))
)
print(f'Actual chi^2: {actual_chi2}')

k = len(b)
l = 1
expected_xhi2 = 13.3

print(f'k:         {k}')
print(f'l:         {l}')
print(f'k - l - 1: {k - l - 1}')
print(f'1 - alpha: {1 - alpha}')
print(f'xhi ^ 2:   {expected_xhi2}')

print(f'(actual vs. expected): ({actual_chi2} vs. {expected_xhi2})')
print('Acceptable!')