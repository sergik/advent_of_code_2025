file_path = "input.txt"

with open(file_path, "r") as f:
    lines = [line.rstrip("\n") for line in f if line.strip()]

# Parse each line by splitting on whitespace. Convert numeric tokens to ints when possible.
grid = []
for line in lines:
    tokens = line.split()
    row = []
    for t in tokens:
        row.append(t)
    grid.append(row)

col_count = len(grid[0])

sum = 0
for c in range(col_count):
    sign = grid[-1][c]
    val = 1 if sign == '*' else 0
    for r in range(len(grid) - 1):
        if sign == '*':
            val *= int(grid[r][c])
        else:
            val += int(grid[r][c])
    sum += val
print(sum)

