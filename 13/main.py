from sympy.ntheory import isprime
count = 100000

num = [0]*count*2
num[1] = 1
num[3] = 1

primesum = 0
primecount = 0

for i in range(1, count):
    if num[i] == 1:
        if isprime(i):
            primesum += i
            primecount += 1
            if primecount == 100:
                break
        for j in range(1, i):
            if num[j] == 1 and i != j:
                num[i+j] += 1

print(primesum, primecount)
