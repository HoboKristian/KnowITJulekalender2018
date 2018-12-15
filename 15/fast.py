count = 0
for line in open("./input-gullbursdag.txt"):
    A = int(line.split(".")[1].strip())
    B = A
    while 1:
        B += 1
        lhs = (B - A)**2
        if lhs == B:
            count += 1
        elif lhs > B:
            break
print(count)
