import numpy

def sieve(n):
    total = numpy.ones(n, dtype=numpy.uint16)
    for i in range(2, n):
        if i % 2**16 == 0:
            print(i)
        if total[i] == 1:
            total[i*i::i] += 1
    return total#numpy.flatnonzero(total)

primes = sieve(2**32)
unique, counts = numpy.unique(primes, return_counts=True)
pfcounts = dict(zip(unique, counts))
print(pfcounts)
