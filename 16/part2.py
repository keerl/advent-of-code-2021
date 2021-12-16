import numpy as np

# Real Input
with open("input.txt") as f:
    INPUT_HEX = [line.rstrip() for line in f][0]

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
    p_version, input = read(3, input)
    p_type, input = read(3, input)

    values = []

    if p_type == 4:
        p_literal, input = read_literal(input)
        return input, p_literal
    else:
        length_type_id, input = read(1, input)

        if length_type_id == 0:
            length, input = read(15, input)
            sub_packet = input[:length]
            while len(sub_packet) > 0:
                unique = list(set(sub_packet))
                if len(unique) == 1 and unique[0] == "0":
                    break
                sub_packet, value = parse(sub_packet, code+1)
                values.append(value)
            input = input[length:]
        elif length_type_id == 1:
            length, input = read(11, input)
            for _ in range(length):
                input, value = parse(input, code+1)
                values.append(value)

        if p_type == 0:
            return input, sum(values)
        elif p_type == 1:
            return input, np.prod(values)
        elif p_type == 2:
            return input, min(values)
        elif p_type == 3:
            return input, max(values)
        elif p_type == 5:
            if values[0] > values[1]:
                return input, 1
            else:
                return input, 0
        elif p_type == 6:
            if values[0] < values[1]:
                return input, 1
            else:
                return input, 0
        elif p_type == 7:
            if values[0] == values[1]:
                return input, 1
            else:
                return input, 0

# INPUT_HEX = "C200B40A82"
# INPUT_HEX = "04005AC33890"
# INPUT_HEX = "880086C3E88112"
# INPUT_HEX = "CE00C43D881120"
# INPUT_HEX = "D8005AC2A8F0"
# INPUT_HEX = "F600BC2D8F"
# INPUT_HEX = "9C005AC2F8F0"
# INPUT_HEX = "9C0141080250320F1802104A08"

# Parse hex/binary stuff
h_size = len(INPUT_HEX) * 4
INPUT = ( bin(int(INPUT_HEX, 16))[2:] ).zfill(h_size)

# Parse
packet, value = parse(INPUT, 0)
print(value)