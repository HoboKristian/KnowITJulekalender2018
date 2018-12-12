with open("tmp.txt") as f:
    txt = f.read().strip()
    s = ""
    for i in range(0, len(txt), 2):
        h = txt[i] + txt[i+1]
        number = int(h, 16)
        s += str(chr(number-96))
    print(s)

