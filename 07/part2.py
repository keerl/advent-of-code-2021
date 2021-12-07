import numpy as np
import math

# Example Input
with open("example.txt") as f:
    lines = [line.rstrip() for line in f]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

data = [int(i) for i in lines[0].split(',')]

# calculated mean rounded is 475 but that is wrong?
# could be rounded down too? checking both vals
mean_upper = int(round(np.mean(data)))
mean_lower = math.floor(np.mean(data))

answers = []

for mean in [mean_upper, mean_lower]:
    fuel = 0
    for point in data:
        tmp = 0
        prev = 0

        add = int(abs(point-mean))
        for i in range(1, add+1):
            prev = i+prev
        fuel += prev

    answers.append(fuel)

print(f"ANS: {min(answers)}")
# 