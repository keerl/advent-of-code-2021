import numpy as np
from collections import Counter

# Example Input
# with open("example.txt") as f:
#     lines = [line.rstrip() for line in f]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]


template = lines[0]
rules = {}
freq_expanded = {}
freq_simple = {}

for line in lines:
    if "->" in line:
        x,y = line.split(" -> ")
        rules[x] = y

for idx in range(len(template)-1):
    if idx % 2 == 0:
        if template[idx] + template[idx+1] in freq_simple:
            freq_simple[template[idx] + template[idx+1]] += 1
        else:
            freq_simple[template[idx] + template[idx+1]] = 1
    if template[idx] + template[idx+1] in freq_expanded:
        freq_expanded[template[idx] + template[idx+1]] += 1
    else:
        freq_expanded[template[idx] + template[idx+1]] = 1

last = template[-1]

count = Counter(template)

print(freq_expanded)
print()

for i in range(40):
    updated_freq_expanded = {}

    for bla in freq_expanded:
        size = freq_expanded[bla]

        val1 = bla[0] + rules[bla]
        val2 = rules[bla] + bla[1]

        if rules[bla] in count:
            count[rules[bla]] += size
        else:
            count[rules[bla]] = size

        if val1 in updated_freq_expanded:
            updated_freq_expanded[val1] += size
        else:
            updated_freq_expanded[val1] = size

        if val2 in updated_freq_expanded:
            updated_freq_expanded[val2] += size
        else:
            updated_freq_expanded[val2] = size

    freq_expanded = updated_freq_expanded

count_min = min(count, key=count.get)
count_max = max(count, key=count.get)
print(count[count_max]-count[count_min])