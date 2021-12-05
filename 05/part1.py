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

    # if len(hori) > 0:
    #     print("HERE")
    #     for coord in hori:
    #         print(f"{coord},{line[0][1]}")
    #         matrix[line[0][1]][coord] += 1
    # else:
    #     print("HERE2", vert)
    #     for coord in vert:
    #         print(f"{coord},{line[0][1]}")
    #         matrix[coord][line[0][0]] += 1

# print(matrix)

print((matrix > 1).sum())