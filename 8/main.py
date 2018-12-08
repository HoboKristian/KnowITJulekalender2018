dolls = []
for line in open("./input-dolls.txt"):
    line = line.strip()
    c, l = line.split(",")
    dolls.append((c, int(l)))

dolls = sorted(dolls, lambda x: x[1])
stack = [dolls[0]]

for candidate in dolls[1:]:
    if candidate[0] != stack[-1][0]:
        if candidate[1] > stack[-1][1]:
            stack.append(candidate)

print(stack, len(dolls), len(stack))

for i in dolls:
    print(i)
