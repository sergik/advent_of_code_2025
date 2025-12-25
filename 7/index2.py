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

beam_positions = {sj: 1}
for i in range(1, len(grid)):
    new_beam_positions = {}
    for j in beam_positions:
        if grid[i][j] == '^':
            if(j -1 >= 0):
                if j - 1 in new_beam_positions:
                    new_beam_positions[j-1] = new_beam_positions[j-1] + beam_positions[j]
                else:
                    new_beam_positions[j-1] = beam_positions[j]
            if(j + 1 < len(grid[i])):
                if j + 1 in new_beam_positions:
                    new_beam_positions[j+1] = new_beam_positions[j+1] + beam_positions[j]
                else:
                    new_beam_positions[j+1] = beam_positions[j]
        else:
            if j in new_beam_positions:
                new_beam_positions[j] = new_beam_positions[j] + beam_positions[j]
            else:    
                new_beam_positions[j] = beam_positions[j]
    beam_positions = new_beam_positions

timelines_count = 0

for j in beam_positions:
    timelines_count += beam_positions[j]
print(timelines_count)


