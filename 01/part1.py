# Example
# lines = [
#     199,
#     200,
#     208,
#     210,
#     200,
#     207,
#     240,
#     269,
#     260,
#     263
# ]

# Real Input
with open("input.txt") as f:
    lines = [int(line.rstrip()) for line in f]

count_increased = 0
count_decreased = 0

for idx, line in enumerate(lines):
    if idx == 0:
        continue

    diff = lines[idx] - lines[idx-1]

    if diff > 0:
        count_increased += 1
    elif diff < 0:
        count_decreased += 1

print(f"COUNT INCREASED {count_increased}")
print(f"COUNT DECREASED {count_decreased}")
