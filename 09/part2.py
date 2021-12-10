import numpy as np
from scipy.ndimage import measurements

# Example Input
# with open("example.txt") as f:
#     lines = [line.rstrip() for line in f]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

matrix = []
for idx, line in enumerate(lines):
    # Replace all non-9 values with 1 (this doesn't really matter)
    # Replace all 9's with 0's
    # This allows for Scipy magic
    data = [0 if i == "9" else 1 for i in list(line)]
    matrix.append(data)

# The magic scipy function. Find clusters ignoring 0's
# That's why 9's were replaced with 0s
lw, num = measurements.label(matrix)

# Example output:
# [[1 1 0 0 0 2 2 2 2 2]
#  [1 0 3 3 3 0 2 0 2 2]
#  [0 3 3 3 3 3 0 4 0 2]
#  [3 3 3 3 3 0 4 4 4 0]
#  [0 3 0 0 0 4 4 4 4 4]]

B = []
for i in range(num):
    # Count the size of each cluster
    B.append(len(lw[lw == i+1]))

B.sort()
B.reverse()
print(B[:3])
print(np.prod(B[:3]))
