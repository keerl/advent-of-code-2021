import numpy as np

# Example Input
with open("example.txt") as f:
    lines = [line.rstrip() for line in f]

# Real Input
with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

data = []

for line in lines:
    data.append(line.split("-"))

routes = []

count = 0

def first_duplicate(a):
    set_ = set()
    for item in a:
        if item in set_:
            return item
        set_.add(item)
    return None

def find_route(find, route_list):
    global count
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
            new_list = route_list.copy()

            if p2 == "end":
                new_list.append(p2)
                routes.append("".join(new_list))
                continue
            else:
                first_dup = first_duplicate(visited)

                if p2 in visited and first_dup != None:
                    continue
                else:
                    new_list.append(p2)

                    res = find_route(p2, new_list)
                    if len(res) == 0:
                        if p1 not in visited:
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

print("Finished, gotta remove duplicates now.")

seen = set()
dupes = []

for i, doi in enumerate(routes):
    print(f"{((i+1)/len(routes))*100}")
    if doi not in seen:
        seen.add(doi)
    else:
        dupes.append(i)

print(len(seen))