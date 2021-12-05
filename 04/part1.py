import re
import numpy as np

# Example
# lines = [
# "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
# "",
# "22 13 17 11  0",
# " 8  2 23  4 24",
# "21  9 14 16  7",
# " 6 10  3 18  5",
# " 1 12 20 15 19",
# "",
# " 3 15  0  2 22",
# " 9 18 13 17  5",
# "19  8  7 25 23",
# "20 11 10 24  4",
# "14 21 16 12  6",
# "",
# "14 21 17 24  4",
# "10 16 15  9 19",
# "18  8 23 26 20",
# "22 11 13  6  5",
# " 2  0 12  3  7"
# ]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

numbers = [int(i) for i in lines[0].split(',')]

################
# Build Boards
################
boards = []
tmp_board = []

for idx, line in enumerate(lines[1:]):
    if line == "":
        if idx != 0:
            boards.append(tmp_board)
            tmp_board = []
        continue
    
    board_line = [int(i) for i in re.sub("\s\s+", " ", line).strip().split(" ")]
    tmp_board.append(board_line)

    if idx == len(lines[1:])-1:
        boards.append(tmp_board)
        tmp_board = []

boards = np.array(boards)

################
# Process Boards
################

winner_board = None
last_number = None

for number in numbers:
    if winner_board is not None:
        break

    # Update boards
    boards = np.where(boards == number, np.nan, boards)

    # Check boards
    for board in boards:
        completed_row = np.isnan(board).all(axis=1).any()
        completed_col = np.isnan(board).all(axis=0).any()

        if (completed_row or completed_col):
            winner_board = board
            last_number = number
            break

print("winner board")
print(winner_board)
print(last_number)

print(int(np.nansum(winner_board)*last_number))

