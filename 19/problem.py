import numpy as np
import itertools
 
# Example Input
with open("example.txt") as f:
    lines = [line.rstrip() for line in f]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

scanners = []

tmp = []
for line in lines:
    if "---" in line:
        pass
    elif line == "":
        scanners.append(np.array(tmp))
        tmp = []
    else:
        coords = [int(i) for i in line.split(',')]
        tmp.append(coords)

scanners.append(np.array(tmp))
tmp = []

def rotations(array):
    for x, y, z in itertools.permutations([0, 1, 2]):
        for sx, sy, sz in itertools.product([-1, 1], repeat=3):
            rotation_matrix = np.zeros((3, 3))
            rotation_matrix[0, x] = sx
            rotation_matrix[1, y] = sy
            rotation_matrix[2, z] = sz
            if np.linalg.det(rotation_matrix) == 1:
                yield np.matmul(rotation_matrix, array)

def get_combinations(scanner):
    combinations = []

    for R in scanner:
        for idx, item in enumerate(rotations(R)):
            if len(combinations) < idx+1:
                combinations.append([])
            combinations[idx].append(item)

    combinations = np.array(combinations).astype(int)
    return combinations

coords_scanners = {}
coords_scanners[0] = [0,0,0]

combined_scanner = scanners[0]

def matching_rows(A,B):
    matches=[i for i in range(B.shape[0]) if np.any(np.all(A==B[i],axis=1))]
    if len(matches)==0:
        return B[matches]
    return np.unique(B[matches],axis=0)

def find_pair():
    global coords_scanners
    global combined_scanner

    for _, current in enumerate(combined_scanner):
        current_offset = current

        tmp_current_scanner = combined_scanner.copy()
        tmp_current_scanner[:, 0] -= current_offset[0]
        tmp_current_scanner[:, 1] -= current_offset[1]
        tmp_current_scanner[:, 2] -= current_offset[2]

        for idx, scanner in enumerate(scanners):
            if idx in coords_scanners.keys():
                continue

            combinations = get_combinations(scanner)

            for combination in combinations:
                for i, _ in enumerate(combination):
                    tmp_combination = combination.copy()

                    offset_x = combination[i][0]
                    offset_y = combination[i][1]
                    offset_z = combination[i][2]

                    tmp_combination[:, 0] -= offset_x
                    tmp_combination[:, 1] -= offset_y
                    tmp_combination[:, 2] -= offset_z

                    m = (tmp_combination[:, None] == tmp_current_scanner).all(-1).any(1)

                    match_count = len(tmp_combination[m])
                    if match_count >= 12:
                        match_all = tmp_combination + [current_offset]

                        for beacon in match_all:
                            if list(beacon) not in combined_scanner:
                                np.append(combined_scanner, beacon)

                        combined_scanner = np.concatenate((combined_scanner, match_all), axis=0)
                        combined_scanner = np.unique(combined_scanner, axis=0)

                        coords_scanners[idx] = [
                            current_offset[0]-offset_x, 
                            current_offset[1]-offset_y, 
                            current_offset[2]-offset_z
                        ]
                        return

def manhattan_distance(a, b):
	return sum(abs(e1-e2) for e1, e2 in zip(a,b))

while len(coords_scanners) != len(scanners):
    find_pair()
    print(f"{len(combined_scanner)} unique beacons (so far)")

print(coords_scanners)

distances = []
for i, point1 in coords_scanners.items():
    for j, point2 in coords_scanners.items():
        distances.append(manhattan_distance(point1, point2))

print(f"Mix distance: {max(distances)}")
