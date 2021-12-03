# Example
lines = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]

# Real Input
# with open("input.txt") as f:
#     lines = [line.rstrip() for line in f]

ones_count = 0
zeros_count = 0

gamma = ""

for row in range(len(lines[0])):
    for column in range(len(lines)):
        if lines[column][row] == "1":
            ones_count += 1
        else:
            zeros_count += 1
    print(ones_count)
    print(zeros_count)
    print()
    if ones_count > zeros_count:
        gamma += '1'
    else:
        gamma += '0'

    ones_count = 0
    zeros_count = 0
    # print()


epsilon = ""

for x in gamma:
    if x == '1':
        epsilon += '0'
    else:
        epsilon += '1'

print(gamma)
print(epsilon)
print(int(gamma, 2))
print(int(epsilon, 2))

print(int(gamma, 2) * int(epsilon, 2))