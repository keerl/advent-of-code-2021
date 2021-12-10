import numpy as np

# Example Input
with open("example.txt") as f:
    lines = [line.rstrip() for line in f]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

invalids = []
scores = []

for line in lines:
    opened = []
    valid = True
    for c in line:
        # print(c)
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
                valid = False
                break
    if valid:
        print(line)
        # print(opened)
        for idx, open in enumerate(opened):
            if open == "(":
                opened[idx] = ")"
            elif open == "[":
                opened[idx] = "]"
            elif open == "{":
                opened[idx] = "}"
            elif open == "<":
                opened[idx] = ">"
        opened.reverse()

        score = 0
        for open in opened:
            if open == ")":
                score = score * 5 + 1
            elif open == "]":
                score = score * 5 + 2
            elif open == "}":
                score = score * 5 + 3
            elif open == ">":
                score = score * 5 + 4
        scores.append(score)
        # line += "".join(opened)
        # print(line)
scores.sort()
print(scores)
print(scores[int(len(scores)/2)])
