import math
import itertools

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def main():
    cities = {
            "a": (7.1, 10.5),
            "b": (18.8, 9.2),
            "c": (2.1, 62.1),
            "d": (74.2, 1.5),
            "e": (58.4, 5.6),
            "f": (15.9, 6.2),
            "g": (44.5, 15.6),
            "h": (88.1, 53.4),
            "i": (36.2, 84.2),
            "j": (26.9, 8.5)}

    distances = {}

    for k1 in cities.keys():
        for k2 in cities.keys():
            distances[k1+k2] = dist(cities[k1], cities[k2])

    best = 10e10
    for possibility in itertools.permutations("abcdefghij"):
        trip = 0
        for i in range(len(possibility) - 1):
            trip += distances[possibility[i]+possibility[i+1]]
        if trip < best:
            best = trip
            print(best)
    print(best)

main()
