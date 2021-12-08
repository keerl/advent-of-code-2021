import numpy as np

# Example Input
# with open("example.txt") as f:
#     lines = [line.rstrip() for line in f]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

total = 0

for line in lines:
    parsed = line.split(" | ")
    segs = parsed[0].split(" ")
    message = parsed[1].split(" ")

    ans_map = {}

    while len(segs) > 0:
        for idx, seg in enumerate(segs):
            length = len(seg)
            if length == 2:
                ans_map["1"] = seg
                segs.pop(idx)
            elif length == 4:
                ans_map["4"] = seg
                segs.pop(idx)
            elif length == 3:
                ans_map["7"] = seg
                segs.pop(idx)
            elif length == 7:
                ans_map["8"] = seg
                segs.pop(idx)
            else:
                if "1" in ans_map and "4" in ans_map and "7" in ans_map and "8" in ans_map:
                    # 2, 3, 5
                    if length == 5:
                        if all(x in list(set(seg)) for x in list(set(ans_map["1"]))):
                            ans_map["3"] = seg
                            segs.remove(seg)
                        else:
                            # 2 or 5
                            chars = list(set(seg).symmetric_difference(set(ans_map["8"])))

                            if all(x in list(set(ans_map["4"])) and x in list(set(ans_map["8"])) for x in chars):
                                ans_map["2"] = seg
                                segs.remove(seg)
                            else:
                                ans_map["5"] = seg
                                segs.remove(seg)
                    elif length == 6:
                        # 0, 6, 9
                        char = list(set(seg).symmetric_difference(set(ans_map["8"])))[0]

                        if (char not in ans_map["1"] and 
                            char not in ans_map["7"] and 
                            char in ans_map["4"] and 
                            char in ans_map["8"]):
                            ans_map["0"] = seg
                            segs.remove(seg)

                        if char not in ans_map["1"] and char not in ans_map["7"] and char not in ans_map["4"] and char in ans_map["8"]:
                            ans_map["9"] = seg
                            segs.remove(seg)

                        if char in ans_map["1"] and char in ans_map["7"] and char in ans_map["4"] and char in ans_map["8"]:
                            ans_map["6"] = seg
                            segs.remove(seg)

    tmp_num = ""
    for number in message:
        for key, value in ans_map.items():
            diff_len = len(list(set(number).symmetric_difference(set(value))))
            if diff_len == 0:
                tmp_num += key
    total += int(tmp_num) 

print(total)