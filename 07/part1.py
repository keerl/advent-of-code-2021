import numpy as np

# Example Input
with open("example.txt") as f:
    lines = [line.rstrip() for line in f]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

data = [int(i) for i in lines[0].split(',')]

median = np.median(data)

fuel = 0
for point in data:
    fuel += abs(point-median)

print(int(fuel))
