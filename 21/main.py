import numpy
from sympy import divisors

def sieve(n):
    flags = numpy.ones(n, dtype=bool)
    flags[0] = flags[1] = False
    for i in range(2, int(n**(1/2))+1):
        # We could use a lower upper bound for this loop, but I don't want to bother with
        # getting the rounding right on the sqrt handling.
        if flags[i]:
            flags[i*i::i] = False
    return flags

limit = 10**7
primes = sieve(limit)

s = 0
for i in range(1, limit, 2):
    if primes[i] and primes[i+2]:
        num = i + 1
        if sum(divisors(num)) - num > num:
            s += num

print(s)
