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

split_total = 0
beam_positions = {sj}
for i in range(1, len(grid)):
    new_beam_positions = set()
    for j in beam_positions:
        if grid[i][j] == '^':
            if(j -1 >= 0):
                new_beam_positions.add(j-1)
            if(j +1 < len(grid[i])):
                new_beam_positions.add(j+1)
            split_total += 1
        else:
            new_beam_positions.add(j)
    beam_positions = new_beam_positions

print(split_total)


