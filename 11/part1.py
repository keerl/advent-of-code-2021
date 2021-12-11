import numpy as np
from itertools import permutations

# Example Input
with open("example.txt") as f:
    lines = [line.rstrip() for line in f]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

# data = [int(i) for i in lines[0].split(',')]

matrix = []
for line in lines:
    tmp = []
    for c in line:
        tmp.append(int(c))
    matrix.append(tmp)
    tmp = []

matrix = np.array(matrix)
print(matrix)

steps = 100
flash_counter = 0

for i in range(steps):
    # step 1
    matrix += 1

    flashed = []

    D = [
        (0,1),
        (0,-1),
        (1,0),
        (-1,0),
        (-1,1),
        (-1,-1),
        (1,1),
        (1,-1),
    ]

    def flash(r,c):
        for dr, dc in D:
            # print(f"({r+dr},{c+dc}): {matrix[dr][dc]}")
            if r+dr < len(matrix) and c+dc < len(matrix[0]) and r+dr >= 0 and c+dc >= 0:
                if [r+dr,c+dc] not in flashed and matrix[r+dr][c+dc] <= 9:
                    matrix[r+dr][c+dc] += 1
                    if matrix[r+dr][c+dc] > 9:
                        flashed.append([r+dr,c+dc])
                        flash(r+dr,c+dc)


    rows, cols = np.where(matrix > 9)
    coords = list(zip(rows, cols))

    for r, c in coords:
        flashed.append([r,c])
        flash(r,c)

    rows, cols = np.where(matrix > 9)
    coords = list(zip(rows, cols))
    for r, c in coords:
        matrix[r][c] = 0

    print(matrix)
    flash_counter += len(np.where(matrix == 0)[0])
    print(flash_counter)
    print()

    # Increase neighboring values

# print(matrix)

