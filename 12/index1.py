file_path = "input.txt"

from collections import deque

with open(file_path, "r") as f:
    lines = [line.rstrip('\n') for line in f if line.rstrip('\n') != ""]

data = [line.split(" ") for line in lines]

graph = {}
for path in data:
    from_key = path[0][0:len(path[0])-1]
    to_keys = path[1:len(path)]
    if from_key not in graph:
        graph[from_key] = []
    for to_key in to_keys:
        graph[from_key].append(to_key)

found_paths = set()
def solve_recursive(next, path):
    if next == "out":
        found_paths.add("".join(path))
        return
    for neighbor in graph.get(next, []):
        if neighbor in path:
            continue
        path.append(neighbor)
        solve_recursive(neighbor, path)
        path.pop()


solve_recursive("you", ["you"])
print(len(found_paths))









