import sys

a = [0]
for i in open("input-vekksort.txt"):
    i = int(i)
    if i >= a[-1]:
        a.append(i)
print(a)
print(sum(a))
