from sympy.ntheory import factorint

tot = 0
for i in range(2**21):
    if i % 10**6 == 0:
        print(i, tot)
    count = len(factorint(i, limit = 512, multiple = True))
    if count == 13:
        tot += 1

print(tot)
