import numpy as np
from itertools import permutations
 

# Example Input
with open("example.txt") as f:
    lines = [line.rstrip() for line in f]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

_, _, x, y = lines[0].split(" ")
x = x.replace("x=", "").replace(",", "")
x = x.split("..")
x = [int(i) for i in x]

y = y.replace("y=", "").replace(",", "")
y = y.split("..")
y = [int(i) for i in y]

def path(v_x,v_y, p_x, p_y):
    return [p_x+v_x, p_y+v_y]


def launch(v):
    p = [0,0]
    while True:
        p = path(v[0], v[1], p[0], p[1])

        if v[0] > 0:
            v[0] -= 1
        elif v[0] < 0:
            v[0] += 1
        v[1] -= 1

        if p[0] >= x[0] and p[0] <= x[1] and p[1] >= y[0] and p[1] <= y[1]:
            return p
        elif p[0] > x[1] or p[1] < min(y):
            return None

I = []
S = 600
for cx in range(1, S):
    for cy in range(-S, S):
        p = launch([cx,-cy])
        if p is not None:
            I.append(p)

print(len(I))