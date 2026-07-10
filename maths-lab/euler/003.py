# Project Euler 3: Largest prime factor of 600851475143
n = 600851475143
f = 2
while f * f <= n:
    if n % f == 0:
        n //= f
    else:
        f += 1
print(n)
