file_path = "input.txt"


def read_grid(path):
    with open(path, "r") as f:
        # keep non-empty lines (strip only the trailing newline so dots are preserved)
        lines = [line.rstrip('\n') for line in f if line.rstrip('\n') != ""]

    grid = [list(line) for line in lines]
    return grid

def find_start_index(grid): 
    for j in range(len(grid[0])):
        if grid[0][j] == 'S':
            return (0, j)
    return None

grid = read_grid(file_path)
si, sj = find_start_index(grid)

timelines = set()
visited = set()
def spread_recursive(i, j, path):
    if i == len(grid):
        timelines.add('_'.join(map(str, path)))
        return
    path.append(j)
    key = '_'.join(map(str, path))
    if key in visited:
        return
    else:
        visited.add(key)
    if(grid[i][j] == '^'):
        if(j -1 >= 0):
            spread_recursive(i+1, j-1, path)
        if(j +1 < len(grid[i])):
            spread_recursive(i+1, j+1, path)
    else:
        spread_recursive(i+1, j, path)

spread_recursive(1, sj, [])
print(len(timelines))


