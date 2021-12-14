import numpy as np

# Example Input
with open("example.txt") as f:
    lines = [line.rstrip() for line in f]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

coords = []
folds_x = []
folds_y = []

for i in lines:
    if "," in i:
        x,y = i.split(",")
        coords.append([int(x), int(y)])
    elif "fold along x=" in i:
        folds_x.append(int(i.split("=")[1]))
    elif "fold along y=" in i:
        folds_y.append(int(i.split("=")[1]))

coords = np.array(coords)
xmax, ymax = coords.max(axis=0)

if not (xmax/2).is_integer():
    xmax += 1
elif not (ymax/2).is_integer():
    ymax += 1

paper = np.zeros((ymax+1, xmax+1))

for x, y in coords:
    paper[y][x] = 1

M = paper

for fold_y in folds_y:
    m1 = M[0:fold_y:, ]
    m2 = np.flipud(M[fold_y+1:, :])
    M = m1 + m2

for fold_x in folds_x: 
    m1 = M[:, 0:fold_x:]
    m2 = np.fliplr(M[:, fold_x+1:])
    M = m1 + m2

# Make readable
answer = []
for r in M:
    tmp = ""
    for c in r:
        if c > 0:
            tmp += "X"
        else:
            tmp += " "
    answer.append(tmp)

for row in answer:
    print(row)
