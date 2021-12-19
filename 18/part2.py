import numpy as np
import math
import ast
 

# Example Input
with open("example.txt") as f:
    lines = [line.rstrip() for line in f]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]


def reduce(x, level):
    for idx, bla in enumerate(x):
        is_list = isinstance(bla, list)

        if is_list:
            if len(level) >= 4:
                return bla, level

            tmp_level = level
            tmp_level.append(idx)
            original, level = reduce(bla, tmp_level)
            return original, level

def magnitude(number):
    is_list = isinstance(number, list)
    if is_list:
        return 3*number[0] + 2*number[1]
    else:
        return number

def process(x, level):
    for idx, bla in enumerate(x):
        is_list = isinstance(bla, list)

        if is_list:
            if isinstance(bla[0], int) and isinstance(bla[1], int):
                calc = magnitude(bla)
                tmp_level = level
                tmp_level.append(idx)
                return (bla, calc)
            else:
                tmp_level = level
                tmp_level.append(idx)
                original, value = process(bla, tmp_level)
                return (original, value)

def find_left(input, index):
    index -= 1
    while index > 0:
        val = input[index]
        if val != "[" and val != "]" and val != ",":
            return index
        index -= 1
    return None

def find_right(input, index):
    index += 1
    while index < len(input):
        val = input[index]
        if val != "[" and val != "]" and val != ",":
            return index
        index += 1
    return None


def explode(input):
    input = str(input).replace(" ", "")
    input_arr = []
    for idx, x in enumerate(input):
        if len(input_arr) > 0:
            if input_arr[-1].isnumeric() and x.isnumeric():
                input_arr[-1] += x
            else:
                input_arr.append(x)
        else:
            input_arr.append(x)

    for idx, x in enumerate(input_arr):
        if x != "[" and x != "]" and x != ",":
            input_arr[idx] = int(x)

    while True:
        before = input_arr.copy()
        nest_count = 0
        for idx, item in enumerate(input_arr):
            if item == "[":
                nest_count += 1
            elif item == "]":
                nest_count -= 1
            else:
                if nest_count >= 5:
                    val1 = input_arr[idx]
                    val2 = input_arr[idx+2]

                    input_arr[idx-1] = 0
                    input_arr[idx] = "X"
                    input_arr[idx+1] = "X"
                    input_arr[idx+2] = "X"
                    input_arr[idx+3] = "X"

                    input_arr = [i for i in input_arr if i != "X"]

                    left_index = find_left(input_arr, idx-1)
                    right_index = find_right(input_arr, idx-1)

                    if left_index:
                        input_arr[left_index] += val1
                    if right_index:
                        input_arr[right_index] += val2

                    # tmp = ""
                    # for x in input_arr:
                    #     if x != "[" and x != "]" and x != ",":
                    #         tmp += str(x)
                    #     else:
                    #         tmp += x
                    # print(tmp)

                    break
        if before == input_arr:
            tmp = ""
            for x in input_arr:
                if x != "[" and x != "]" and x != ",":
                    tmp += str(x)
                else:
                    tmp += x
            return tmp

input = "[[[[[9,8],1],2],3],4]"
input = "[7,[6,[5,[4,[3,2]]]]]"
input = "[[6,[5,[4,[3,2]]]],1]"
input = "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
# input = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"

# print("EXPLODE", explode(input))

def split_up(input):
    input = str(input).replace(" ", "")
    input_arr = []
    for idx, x in enumerate(input):
        if len(input_arr) > 0:
            if input_arr[-1].isnumeric() and x.isnumeric():
                input_arr[-1] += x
            else:
                input_arr.append(x)
        else:
            input_arr.append(x)

    for idx, x in enumerate(input_arr):
        if x != "[" and x != "]" and x != ",":
            input_arr[idx] = int(x)

    for idx, x in enumerate(input_arr):
        if x != "[" and x != "]" and x != ",":
            if x >= 10:
                input_arr[idx] = [math.floor(x/2), math.ceil(x/2)]
                break

    tmp = ""
    for x in input_arr:
        if x != "[" and x != "]" and x != ",":
            tmp += str(x)
        else:
            tmp += x
    return tmp

def mag(input):
    input = str(input).replace(" ", "")

    while True:
        number = ast.literal_eval(input)
        if isinstance(number[0], int) and isinstance(number[1], int):
            calc = magnitude(number)
            return calc

        original, value = process(number, [0])
        input = input.replace(str(original).replace(" ", ""), str(value))

mags = []

for idx, line in enumerate(lines):
    for jdx, line2 in enumerate(lines):
        val1 = ast.literal_eval(line)
        val2 = ast.literal_eval(line2)

        add = [val1, val2]

        while True:
            before = add
            add = explode(add)
            add = split_up(add)
            if before == add:
                break
        
        mags.append(mag(add))


print(max(mags))



