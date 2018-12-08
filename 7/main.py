x = []
for line in open("input-vekksort.txt"):
    x.append(int(line))

y=[x[i]+i/len(x) for i in range(len(x))]
print(y)

exit(0)

curr_len = []

c = 0

for i in input_list:
    c += 1
    if c % 10**5 == 0:
        print(c)
    current_best = (0, i)
    for ind in range(len(curr_len)):
        l = curr_len[ind]
        m = input_list[ind]
        if m <= i and l > current_best[0]:
            current_best = (l, m)
    curr_len.append(current_best[0] + 1)

print(curr_len)
print(max(curr_len))
