import numpy as np
from collections import Counter
import tcod
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path
import networkx as nx

# Example Input
with open("example.txt") as f:
    lines = [line.rstrip() for line in f]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

G = {}

rows = len(lines)
cols = len(lines[0])

M = np.zeros((rows,cols))

for r, line in enumerate(lines):
    for c, char in enumerate(line):
        top = (r-1,c)
        bottom = (r+1,c)
        left = (r,c-1)
        right = (r,c+1)

        G[(r,c)] = {}

        for dr, dc in [top, bottom, left, right]:
            if dr >= 0 and dr < rows and dc >= 0 and dc < cols:
                G[(r,c)][(dr,dc)] = int(lines[dr][dc])

# for key, value in G.items():
#     print(key, value)

def dijkstra(graph, start, goal):
    # records the cost to reach that node. continually updated
    shortest = {}
    # keep track of current path
    previous = {}

    unseen_nodes = graph
    infinity = float('inf')   

    path = []

    for node in unseen_nodes:
        shortest[node] = infinity

    shortest[start] = 0

    while len(unseen_nodes) > 0:
        min_distance_node = list(unseen_nodes.keys())[0]

        options = graph[min_distance_node].items()

        for child, weight in options:
            if weight + shortest[min_distance_node] < shortest[child]:
                shortest[child] = weight + shortest[min_distance_node]
                previous[child] = min_distance_node

        unseen_nodes.pop(min_distance_node)

    current_node = goal

    while current_node != start:
        path.insert(0, current_node)
        current_node = previous[current_node]

    path.insert(0, start)

    if shortest[goal] != infinity:
        print(f"Optimal path is {path}")
        print(f"Shortest distance is {shortest[goal]}")


dijkstra(G, (0,0), (rows-1,cols-1))