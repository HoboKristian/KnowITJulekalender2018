def point_to_xy(p):
    x, y = p.split(",")
    return (int(x), int(y))

def coord(s):
    s = s.replace("\n", "")
    s = s.replace("(", "")
    s = s.replace(")", "")

    p1, p2 = s.split(";")

    return (point_to_xy(p1), point_to_xy(p2))

def slope(points):
    p1 = points[0]
    p2 = points[1]

    return (p1[1] - p2[1]) / (p1[0] - p2[0])


def main():
    c = {}
    points = []
    for f in open("input-rain.txt"):
        slop = slope(coord(f))
        tmp = c.get(slop, 0)
        c[slop] = tmp + 1

    print(max([c[a] for a in c]))


main()
