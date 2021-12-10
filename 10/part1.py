import numpy as np

# Example Input
with open("example.txt") as f:
    lines = [line.rstrip() for line in f]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

invalids = []

for line in lines:
    opened = []
    for c in line:
        if c == "(" or c == "[" or c == "{" or c == "<":
            opened.append(c)
        else:
            if c == ")" and opened[-1] == "(":
                opened.pop()
                # print("VALID", opened)
            elif c == "]" and opened[-1] == "[":
                opened.pop()
                # print("VALID", opened)
            elif c == "}" and opened[-1] == "{":
                opened.pop()
                # print("VALID", opened)
            elif c == ">" and opened[-1] == "<":
                opened.pop()
                # print("VALID", opened)
            else:
                invalids.append(c)
                print(line)
                print("INVALID")
                break
    # print("INCOMPLETE")

count = 0
for invalid in invalids:
    if invalid == ")":
        count += 3
    elif invalid == "]":
        count += 57
    elif invalid == "}":
        count += 1197
    elif invalid == ">":
        count += 25137

print(count)