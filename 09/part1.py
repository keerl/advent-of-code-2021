import numpy as np

# Example Input
with open("example.txt") as f:
    lines = [line.rstrip() for line in f]

# Real Input
# with open("input.txt") as f:
#     lines = [line.rstrip() for line in f]

# data = [int(i) for i in lines[0].split(',')]

print(lines)
matrix = []
for idx, line in enumerate(lines):
    data = [int(i) for i in list(line)]
    matrix.append(data)

print(np.array(matrix))
low_points = []
sum = 0
for i, row in enumerate(matrix):
    for j, num in enumerate(row):
        # print(f"{j}:({i}) {num}")
        heights = []

        if j+1 >= 0 and j+1 < len(row):
            heights.append(matrix[i][j+1])
        if j-1 >= 0:
            heights.append(matrix[i][j-1])

        if i+1 >= 0 and i+1 < len(matrix):
            heights.append(matrix[i+1][j])
        if i-1 >= 0:
            heights.append(matrix[i-1][j])

        if all(i > num for i in heights):
            low_points.append([i,j])
            sum += 1 + num
        # print()
print(sum)
print(low_points)
        # if i > 1 and i < len(matrix)-1:
        #     nt = matrix[j][i+1]
        #     nb = matrix[j][i-1]
        #     neighbors.append(nt)
        #     neighbors.append(nb)

        # if j > 1 and j < len(matrix)-1:
        #     nl = matrix[j-1][i]
        #     nr = matrix[j+1][i]
        #     neighbors.append(nl)
        #     neighbors.append(nr)

        # print(neighbors)
        
