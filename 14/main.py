x,y = 0,0
actions = {"H": [1,0],
        "V": [-1,0],
        "F": [0,1],
        "B": [0,-1]}

locs = set()
locs.add((x, y))

txt = open("./input-bounding-crisscross.txt").read().strip()
for i in range(0, len(txt), 2):
    c = int(txt[i])
    a = txt[i+1]
    for j in range(c):
        x += actions[a][0]
        y += actions[a][1]
        locs.add((x, y))

max_x, min_x, max_y, min_y = 0,0,0,0
for l in locs:
    max_x = max(max_x, l[0])
    min_x = min(min_x, l[0])
    max_y = max(max_y, l[1])
    min_y = min(min_y, l[1])

print(max_x, min_x, max_y, min_y)
bounding_box = (max_x-min_x+1)*(max_y-min_y+1)
visited = len(locs)
not_visited = bounding_box - visited
print(f"{bounding_box} {visited} {not_visited} {visited/not_visited:.16f}")
