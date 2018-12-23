import math

def s(elem):
    x, y = elem.split(",")
    return (float(x), float(y))

def coord_to_polar(coord):
    x, y = coord
    rho = math.atan2(y, x)
    return (x, y, rho)

txt = open("./input-luke-22.txt").read().strip().split("\n")
coords = map(s, txt)
polars = map(coord_to_polar, coords)

c = sorted(polars, key=lambda x: x[2])

def dist(one, two):
    x,y,_ = one
    x2,y2,_ = two
    return math.sqrt((x-x2)**2 + (y-y2)**2)

l = dist(c[-1], c[0])
for i in range(1, len(c)):
    l += dist(c[i-1], c[i])

print(l)

