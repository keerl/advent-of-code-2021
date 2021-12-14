import numpy as np
from collections import Counter

# Example Input
with open("example.txt") as f:
    lines = [line.rstrip() for line in f]

# Real Input
# with open("input.txt") as f:
#     lines = [line.rstrip() for line in f]

# data = [int(i) for i in lines[0].split(',')]

template = lines[0]
rules = {}

for line in lines:
    if "->" in line:
        x,y = line.split(" -> ")
        rules[x] = y

# print(template)
# print(rules)

for i in range(4):
    # print(f"BEFORE: {Counter(template)}")
    new = ""
    for idx in range(len(template)):
        if idx+1 == len(template):
            new += template[idx]
            break
        
        pair = template[idx] + template[idx+1]
        new += template[idx] + rules[pair]
        print(f"{pair} -> {rules[pair]}")
    
    # print(len(new)-len(template))
    template = new
    print(f"{Counter(new)}")
    print()
# count = Counter(new)
# print(count)
# count_min = min(count, key=count.get)
# count_max = max(count, key=count.get)
# # min_key, min_count = min(c.items(), key=itemgetter(1))
# print(count[count_max]-count[count_min])