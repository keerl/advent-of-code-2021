import numpy as np

# Example Input
with open("example.txt") as f:
    lines = [line.rstrip() for line in f]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

# data = [int(i) for i in lines[0].split(',')]
data = []

for line in lines:
    data.append(line.split("-"))

routes = []

def find_route(find, route_list):
    visited = [i for i in route_list if i.islower() and i != "start"]
    for r in data:
        # found match
        if r[0] == find or r[1] == find and r[0] != "start" and r[1] != "start":
            if r[0] == find:
                p1 = r[0]
                p2 = r[1]
            else:
                p1 = r[1]
                p2 = r[0]

            if p1 == "start" or p2 == "start":
                continue
            # if len(route_list) > 1:
            #     if route_list[0] == "start" and route_list[1] == "b":
                    # print("HERE", find, r)
                    # print("FOUND", find)
            new_list = route_list.copy()
            # print(f"FOUND MATCH {r} {new_list} {visited}")
            # print(r[0], r[0] in visited)

            if p2 == "end":
                new_list.append(p2)
                if new_list not in routes:
                    routes.append(new_list)
                continue
            else:
                if p2 in visited:
                    continue
                else:
                    new_list.append(p2)
                    if p2.islower():
                        visited.append(p2)

                    res = find_route(p2, new_list)
                    if len(res) == 0:
                        # print("HERE2")
                        if p1 not in visited:
                            # print(f"ADDING {r[0]}")
                            new_list.append(p1)
                            find_route(p1, new_list)
    return []

routes = []
for route in data:
    tmp = []
    if route[0] == "start":
        find_route(route[1], route)
    elif route[1] == "start":
        find_route(route[0], [route[1], route[0]])

# for route in routes:
#     print(route)

print(len(routes))