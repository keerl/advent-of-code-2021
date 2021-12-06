import numpy as np

# Example Input
with open("example.txt") as f:
    lines = [line.rstrip() for line in f]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

times = [int(i) for i in lines[0].split(',')]

days = 256

data = [0]*9
for time in times:
    data[time] += 1

for day in range(days):
    # Reset any fish that created a fish to 6
    data[7] += data[0]
    # Add new fish
    data.append(data[0])

    # Subtract 1 (shift left)
    data.pop(0)

print(sum(data))