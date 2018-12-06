def heavy(num):
    s = str(num)
    return sum([1 if a == "0" else 0 for a in s]) > len(s) // 2

tot = 0
for i in range(0, 18163106):
    if heavy(i):
        tot += i
print(tot)
