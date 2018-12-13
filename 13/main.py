from sympy.ntheory import isprime
count = 100000

num = [0]*count*2
num[1] = 1
num[3] = 1

stack = []

for i in range(1, count):
    if num[i] == 1:
        if isprime(i):
            stack.append(i)
        print(i)
        for j in range(1, i):
            if num[j] == 1 and i != j:
                num[i+j] += 1

print(stack, sum(stack), sum(stack[:100]), len(stack))
