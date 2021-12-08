import numpy as np

# Example Input
# with open("example.txt") as f:
#     lines = [line.rstrip() for line in f]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip().split(" | ")[1] for line in f]

count = {
    "1": 0,
    "4": 0,
    "7": 0,
    "8": 0
}

words = []
for line in lines:
    bla = line.split(" ")
    words.extend(bla)

total = 0 

for word in words:
    length = len(word)
    if length == 2:
        count["1"] += 1
        total += 1
    elif length == 4:
        count["4"] += 1
        total += 1
    elif length == 3:
        count["7"] += 1
        total += 1
    elif length == 7:
        count["8"] += 1
        total += 1

print(count)
print(total)

