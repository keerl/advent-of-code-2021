import numpy as np

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

# Convert to Numpy Matrix (there's probably a better way to do this)
parsed_input = np.zeros((len(lines), len(lines[0])), dtype=int)
for idx, line in enumerate(lines):
    parsed_input[idx] = np.fromstring(line,'u1') - ord('0')

##########
# PART 1 #
##########
gamma_bin = ""
epsilon_bin = ""

processed = parsed_input
for column in range(parsed_input.shape[1]):
    if processed.sum(axis=0)[column] > int(parsed_input.shape[0]/2):
        gamma_bin += "1"
        epsilon_bin += "0"
    else:
        gamma_bin += "0"
        epsilon_bin += "1"

gamma_dec = int(gamma_bin, 2)
epsilon_dec = int(epsilon_bin, 2)

print(f"PART 1 ANSWER: {gamma_dec*epsilon_dec}")

##########
# PART 2 #
##########
answers = []
processed = parsed_input

for i in range(2):
    processed = parsed_input
    for column in range(parsed_input.shape[1]):
        col_sum = processed.sum(axis=0)[column]
        size = processed.shape[0]/2
        if col_sum > size or col_sum == size:
            processed = processed[processed[:, column] == 1-i]
        elif col_sum < size:
            processed = processed[processed[:, column] == i]
        if len(processed) == 1:
            break
    answers.append(int(''.join(map(str, processed[0])), 2))

print(f"PART 2 ANSWER: {np.prod(answers)}")
