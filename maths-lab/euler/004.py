# Project Euler 4: Largest palindrome product of two 3-digit numbers
best = 0
for a in range(100, 1000):
    for b in range(a, 1000):
        p = a * b
        if str(p) == str(p)[::-1] and p > best:
            best = p
print(best)
