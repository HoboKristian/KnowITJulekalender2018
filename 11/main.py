x,y = 0,0

with open("./input-crisscross.txt") as f:
    txt = f.read().strip()
    for i in range(0, len(txt), 2):
        if i % 10e6 == 0:
            print(i)
        n = int(txt[i])
        c = txt[i+1]
        if c == "H":
            x += n
        elif c == "V":
            x -= n
        elif c == "F":
            y += n
        elif c == "B":
            y -= n


print(x,y)
