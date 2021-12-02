# Example
# lines = [
# 	"forward 5",
# 	"down 5",
# 	"forward 8",
# 	"up 3",
# 	"down 8",
# 	"forward 2"
# ]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

horizontal = 0
depth = 0
aim = 0

for line in lines:
    raw_command = line.split(' ')
    direction = raw_command[0]
    value = int(raw_command[1])

    if direction == "forward":
        horizontal += value
        depth += value * aim
    elif direction == "down":
        aim += value
    elif direction == "up":
        aim -= value

print(f"HORIZONTAL: {horizontal}")
print(f"DEPTH: {depth}")

print(f"ANSWER: {horizontal*depth}")