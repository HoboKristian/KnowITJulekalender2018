txt = open("./input.txt").read().strip()

a,b,c = 0,0,0

i = 0
while i < len(txt):
    played = txt[i:i+3]
    if played == "SPR" or played == "SRP" or played == "PSR" or played == "PRS" or played == "RSP" or played == "RPS" or played == "SSS" or played == "RRR" or played == "PPP":
        i += 3
    elif played == "SSR" or played == "RRP" or played == "PPS":
        c += 1
        i += 3
    elif played == "SRS" or played == "RPR" or played == "PSP":
        b += 1
        i += 3
    elif played == "RSS" or played == "PRR" or played == "SPP":
        a += 1
        i += 3
    elif played == "SSP" or played == "RRS" or played == "PPR":
        #omkamp ab
        i += 3
        while 1:
            omkamp = txt[i:i+2]
            i += 2
            if omkamp == "SS" or omkamp == "RR" or omkamp == "PP":
                continue
            if omkamp == "RS" or omkamp == "PR" or omkamp == "SP":
                a += 1
            else:
                b += 1
            break
    elif played == "SPS" or played == "RSR" or played == "PRP":
        #omkarp ac
        i += 3
        while 1:
            omkamp = txt[i:i+2]
            i += 2
            if omkamp == "SS" or omkamp == "RR" or omkamp == "PP":
                continue
            if omkamp == "RS" or omkamp == "PR" or omkamp == "SP":
                a += 1
            else:
                c += 1
            break
    elif played == "PSS" or played == "SRR" or played == "RPP":
        #omkamp bc
        i += 3
        while 1:
            omkamp = txt[i:i+2]
            i += 2
            if omkamp == "SS" or omkamp == "RR" or omkamp == "PP":
                continue
            if omkamp == "RS" or omkamp == "PR" or omkamp == "SP":
                b += 1
            else:
                c += 1
            break
        continue
print(a,b,c)
