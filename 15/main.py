from sympy import Symbol, S, solveset

A = Symbol('A')
B = Symbol('B')

i = 0
for line in open("./input-gullbursdag.txt"):
    i += 1
    if i % 100 == 0:
        print(i)
    year = line.split(".")[1].strip()
    count = 0
    A = int(year)
    for option in solveset((B-A)**2-B, B, domain=S.Naturals):
        if option > A:
            count += 1

print(count)
