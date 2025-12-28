file_path = "input.txt"

from collections import deque, defaultdict

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

graph["out"] = []


def topo_sort(graph):
    indeg = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            indeg[v] += 1

    q = deque([u for u in graph if indeg[u] == 0])
    order = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return order

def count_paths_dag(graph1, A):
    topo = topo_sort(graph)
    ways = defaultdict(int)
    ways[A] = 1

    for u in topo:
        for v in graph1[u]:
            ways[v] += ways[u]

    return ways

ways = count_paths_dag(graph, "svr")

print(ways["out"])

# svr -> fft * fft -> dac * dac -> out







