def s(elem):
    x, y = elem.split(",")
    return (float(x), float(y))

txt = open("./input-luke-22.txt").read().strip().split("\n")
coords = list(map(s, txt))

import numpy as np
import matplotlib.pyplot as plt

x = [a[0] for a in coords]
y = [a[1] for a in coords]

plt.scatter(x, y)
plt.show()
# notice it is a circle with Radius = 1000.
# length = 2000 * pi
