file_path = "example.txt"
with open(file_path, "r") as f:
     grid = [list(line.rstrip("\n")) for line in f if line.strip()]





def neighbors(grid, r, c):
    rows = len(grid)
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < len(grid[nr]):
                yield grid[nr][nc]


# Demo: iterate through the grid and print each cell's neighbors

sum = 0
removes = 1
while removes > 0:
    removes = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if(grid[r][c] != '@'):
                continue
            neigh = list(neighbors(grid, r, c))
            count_at =  neigh.count('@')
            if count_at < 4:
                sum += 1
                removes +=1
                grid[r][c] = '.'
print(sum)
       

