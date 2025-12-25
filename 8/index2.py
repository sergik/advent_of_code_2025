file_path = "input.txt"

class PointsWithDistance:
    def __init__(self, dist, point1, point2):
        self.dist = dist
        self.point1 = point1
        self.point2 = point2
    dist: int
    point1Key:  str
    point2Key:  str

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n   # or use size[]

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]
    
    def get_problem_answer(self) -> int:
        sets_sizes = {}
        for i in range(len(self.parent)):
            val = self.find(i)
            if val not in sets_sizes:
                sets_sizes[val] = 1
            else:
                sets_sizes[val] += 1
        
        values = sets_sizes.values()
        values = sorted(values, reverse=True)

        print(values)
    
        return values[0] * values[1] * values[2]

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False

        # union by rank
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True


with open(file_path, "r") as f:
    data = [list(map(int, line.rstrip('\n').split(','))) for line in f if line.rstrip('\n') != ""]


def distance(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2

def get_point_key(p):
    return f"{p[0]}_{p[1]}_{p[2]}"

index_by_point = {}
for i in range(len(data)):
    index_by_point[get_point_key(data[i])] = i

points_with_distances = []
for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        dist = distance(data[i], data[j])
        points_with_distances.append(PointsWithDistance(dist, get_point_key(data[i]), get_point_key(data[j])))


# sort ascending by distance
points_with_distances.sort(key=lambda p: p.dist)

connections = 0
dsu = DSU(len(data))

last = 0
for p in points_with_distances:
    index1 = index_by_point[p.point1]
    index2 = index_by_point[p.point2]
    if dsu.union(index1, index2):
        cords1 = p.point1.split('_')
        cords2 = p.point2.split('_')
        last = int(cords1[0]) * int(cords2[0])

  
print(last)

