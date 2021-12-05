import numpy as np

# Example
lines = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

parsed = []
for line in lines:
    tmp = []
    coords = line.split(' -> ')
    for coord in coords:
        tmp.append([int(i) for i in coord.split(',')])
    parsed.append(tmp)

matrix = np.zeros((np.amax(parsed)+1, np.amax(parsed)+1))

for line in parsed:
    hori = []
    vert = []

    if line[0][0] == line[1][0]:
        it = [line[0][1], line[1][1]]
        it.sort()
        for x in range(it[0], it[1]+1):
            matrix[x][line[0][0]] += 1
    elif line[0][1] == line[1][1]:
        it = [line[0][0], line[1][0]]
        it.sort()
        for x in range(it[0], it[1]+1):
            matrix[line[0][1]][x] += 1
    else:
        print(line)
        diffx = abs(line[1][0] - line[0][0])
        diffy = abs(line[1][1] - line[0][1])

        minx = min([line[1][0], line[0][0]])
        maxx = minx + diffx
        miny = min([line[1][1], line[0][1]])
        maxy = miny + diffy

        valsX = []
        valsY = []

        if minx == line[0][0]:
            for x in range(minx, maxx+1):
                valsX.append(x)
        else:
            for x in range(maxx, minx-1, -1):
                valsX.append(x)

        if miny == line[0][1]:
            for y in range(miny, maxy+1):
                valsY.append(y)
        else:
            for y in range(maxy, miny-1, -1):
                valsY.append(y)

        comb = list(zip(valsX, valsY))

        for coord in comb:
            matrix[coord[1]][coord[0]] += 1

# print(matrix)

print((matrix > 1).sum())