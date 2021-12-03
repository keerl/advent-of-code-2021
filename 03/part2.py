# Example
# lines = [
#     "00100",
#     "11110",
#     "10110",
#     "10111",
#     "10101",
#     "01111",
#     "00111",
#     "11100",
#     "10000",
#     "11001",
#     "00010",
#     "01010"
# ]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

ones_count = 0
zeros_count = 0

def filter_out(value, column, array):
    print(value)
    print(column)
    tmp = []
    for item in array:
        if item[column] == value:
            tmp.append(item)
    return tmp

count = 0
while len(lines) > 1:
    for column in range(len(lines)):
        if lines[column][count] == "1":
            ones_count += 1
        else:
            zeros_count += 1

    if ones_count >= zeros_count:
        print("MORE ONES")
        lines = filter_out('1', count, lines)
        print(lines)
        print()
    else:
        print("MORE ZEROS")
        lines = filter_out('0', count, lines)

    ones_count = 0
    zeros_count = 0
    count += 1

ox = lines[0]
print(ox)
    # print()

# lines = [
#     "00100",
#     "11110",
#     "10110",
#     "10111",
#     "10101",
#     "01111",
#     "00111",
#     "11100",
#     "10000",
#     "11001",
#     "00010",
#     "01010"
# ]

with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

count = 0
while len(lines) > 1:
    for column in range(len(lines)):
        if lines[column][count] == "1":
            ones_count += 1
        else:
            zeros_count += 1

    if ones_count < zeros_count:
        print("MORE ONES")
        lines = filter_out('1', count, lines)
        print(lines)
        print()
    else:
        print("MORE ZEROS")
        lines = filter_out('0', count, lines)

    ones_count = 0
    zeros_count = 0
    count += 1

co2 = lines[0]
# print(gamma)
# print(epsilon)
# print(int(gamma, 2))
# print(int(epsilon, 2))

print()

print(ox)
print(co2)
print()
print(int(ox, 2))
print(int(co2, 2))
print(int(ox, 2) * int(co2, 2))