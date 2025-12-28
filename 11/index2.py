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

# important_nodes = ["fft", "svr", "dac", "out"]
# visited_nodes = set()
# def visit_nodes_recursive(node):
#     if node in visited_nodes:
#         return
#     visited_nodes.add(node)
#     for neighbor in graph.get(node, []):
#         visit_nodes_recursive(neighbor)
# print(len(graph))
# for node in important_nodes:
    
#     visited_nodes = set()
#     visit_nodes_recursive(node)
#     visited_nodes.add(node)
#     for key in list(graph.keys()):
#         if key not in visited_nodes and key not in important_nodes:
#             if key in graph:
#                 del graph[key]
#     print(len(graph))





found_paths = set()
res = 0
exit = "fft"
visited = set()
forbiden = set()
def solve_recursive(next, path):
    if next in forbiden:
        return
    key = "|".join(path) 
    if next == exit: 
        if  key not in found_paths:
            found_paths.add("|".join(path))
        return
    
    for neighbor in graph.get(next, []):
        if neighbor in path:
            continue
        path.append(neighbor)
        solve_recursive(neighbor, path)
        path.pop()


exit = "dac"
forbiden = set(["srv", "out"])
solve_recursive("fft", ["fft"])
print(len(found_paths))

# exit = "dac"
# found_paths = set()
# visited = set()
# solve_recursive("svr", ["svr"])
print(len(found_paths))





# print(res)









