import numpy as np
import time

# Example Input
with open("example.txt") as f:
    lines = [line.rstrip() for line in f]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

modified_lines = []

for i in range(5):
    for line in lines:
        tmp = []
        for j in range(5):
            for char in line:
                num = (int(char) + i + j - 1) % 9 + 1
                tmp += str(num)
        modified_lines.append(tmp)

lines = modified_lines

G = {}

rows = len(lines)
cols = len(lines[0])

M = np.zeros((rows,cols))

end = (rows-1,cols-1)

for r, line in enumerate(lines):
    for c, char in enumerate(line):
        top = (r-1,c)
        bottom = (r+1,c)
        left = (r,c-1)
        right = (r,c+1)

        G[(r,c)] = {}

        for dr, dc in [top, bottom, left, right]:
            if dr >= 0 and dr < rows and dc >= 0 and dc < cols:
                distance = 1
                G[(r,c)][(dr,dc)] = int(lines[dr][dc]) * distance

def dijkstra(graph, start, goal):
    shortest = {}
    previous = {}
    infinity = float('inf')   

    path = []

    for node in graph:
        shortest[node] = infinity

    shortest[start] = 0
    queue = [(0,0)]

    index = 0

    while queue:
        min_distance_node = queue.pop(0)

        options = graph[min_distance_node].items()

        for child, weight in options:
            dx = abs(int(dr) - int(end[0]))
            dy = abs(int(dc) - int(end[1]))
            distance = dx+dy
            m_weight = weight * distance

            if m_weight + shortest[min_distance_node] < shortest[child]:
                shortest[child] = m_weight + shortest[min_distance_node]
                previous[child] = min_distance_node
                queue.append(child)
        index += 1

    current_node = goal

    while current_node != start:
        path.insert(0, current_node)
        current_node = previous[current_node]

    path.insert(0, start)

    if shortest[goal] != infinity:
        count = 0
        for i, item in enumerate(path):
            if i == 0:
                continue
            count += int(lines[item[0]][item[1]])
        print(count)


t1 = time.time()
dijkstra(G, (0,0), (rows-1,cols-1))
t2 = time.time()
print(t2-t1)