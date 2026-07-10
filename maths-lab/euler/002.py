# Project Euler 2: Even Fibonacci numbers below 4,000,000
a, b, total = 1, 2, 0
while a < 4_000_000:
    if a % 2 == 0:
        total += a
    a, b = b, a + b
print(total)
