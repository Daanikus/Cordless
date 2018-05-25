import sys
from matplotlib import pyplot as plt
import random
import math

P = []
Px = []
Py = []

def distance(a, b):
    xDiff = math.fabs(float(a[0]) - float(b[0]))
    yDiff = math.fabs(float(a[1]) - float(b[1]))
    return math.sqrt(xDiff ** 2 + yDiff ** 2)

def half_way_point(a ,b):
    x = a[0] if a[0] < b[0] else b[0]
    y = a[1] if a[1] < b[1] else b[1]
    xDiff = math.fabs(float(a[0]) - float(b[0]))
    yDiff = math.fabs(float(a[1]) - float(b[1]))
    return [xDiff + float(x),yDiff + float(y)]

for line in sys.stdin:
    split_line = line.split("  ")
    if len(split_line) == 2:
        P.append([split_line[0], split_line[1].strip()])

Px = [i[0] for i in P]
Py = [i[1] for i in P]

for x,y in zip(Px, Py):
    print(x + " " + y)

plt.plot(Px, Py, '.')
a = random.choice(P)
b = random.choice(P)
print(f"A is {a} and B is {b}")
dist = distance(a,b)
centre = half_way_point(a,b)
print(centre)
circle = plt.Circle((centre[0], centre[1]), dist / 2, color='blue', fill=True)
fig = plt.gcf()
ax = fig.gca()
ax.add_artist(circle)
plt.show()
