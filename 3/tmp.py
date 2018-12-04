from sympy.ntheory import factorint

tot = 0
for i in range(2**24, 2**32):
    if i % 2**16 == 0:
        print(i, tot)
    count = len(factorint(i, limit = 512, multiple = True))
    if count == 24:
        tot += 1

print(tot)
