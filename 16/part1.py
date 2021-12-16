import numpy as np

# Real Input
with open("input.txt") as f:
    INPUT_HEX = [line.rstrip() for line in f][0]

V_SUM = 0

def read(size, input):
    data = int(input[0:size], 2)
    input = input[size:]

    return data, input

def read_literal(input):
    number = ""
    while True:
        slice = input[0:5]
        input = input[5:]
        number += slice[1:5]
        if slice[0] == "0":
            break
    return int(number, 2), input

def parse(input, code):
    global V_SUM
    p_version, input = read(3, input)
    V_SUM += p_version
    p_type, input = read(3, input)

    if p_type == 4:
        p_literal, input = read_literal(input)
    else:
        length_type_id, input = read(1, input)

        if length_type_id == 0:
            length, input = read(15, input)
            sub_packet = input[:length]
            while len(sub_packet) > 0:
                unique = list(set(sub_packet))
                if len(unique) == 1 and unique[0] == "0":
                    break
                sub_packet = parse(sub_packet, code+1)
            input = input[length:]
        elif length_type_id == 1:
            length, input = read(11, input)
            for _ in range(length):
                input = parse(input, code+1)

    return input

# INPUT_HEX = "D2FE28"
# INPUT_HEX = "38006F45291200"
# INPUT_HEX = "EE00D40C823060"
# INPUT_HEX = "8A004A801A8002F478"
# INPUT_HEX = "620080001611562C8802118E34"
# INPUT_HEX = "C0015000016115A2E0802F182340"
# INPUT_HEX = "A0016C880162017C3686B18A3D4780"

h_size = len(INPUT_HEX) * 4
INPUT = ( bin(int(INPUT_HEX, 16))[2:] ).zfill(h_size)
parse(INPUT, 0)

print("SUM", V_SUM)