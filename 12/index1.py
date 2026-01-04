import re
from pathlib import Path

file_path = "example.txt"


def parse_shapes_and_bottom(path):
    """Parse file for indexed shapes and trailing dimension lines.

    Returns:
      shapes: dict mapping int index -> 2D list of ints (1 for '#', 0 for '.')
      bottom: list of pairs [[w,h], [ints...]] parsed from lines like '4x4: 0 0 0 0 2 0'
    """
    p = Path(path)
    lines = [ln.rstrip('\n') for ln in p.read_text().splitlines()]

    shapes = {}
    i = 0
    # Parse blocks like:
    # 0:
    # ###
    # ##.
    # ##.
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        m = re.match(r"^(\d+):$", line)
        if m:
            idx = int(m.group(1))
            i += 1
            grid = []
            # collect consecutive rows of # and .
            while i < len(lines) and lines[i].strip() != "":
                row = lines[i].strip()
                if re.match(r"^[#.]+$", row):
                    grid.append([1 if c == "#" else 0 for c in row])
                    i += 1
                else:
                    break
            shapes[idx] = grid
            continue
        # stop when we hit a size: line (e.g. 4x4: ...)
        if re.match(r"^\d+x\d+:", line):
            break
        i += 1

    # Parse the bottom lines from remaining lines
    bottom = []
    for j in range(i, len(lines)):
        line = lines[j].strip()
        if not line:
            continue
        m = re.match(r"^(\d+)x(\d+):\s*(.*)$", line)
        if not m:
            continue
        w, h = int(m.group(1)), int(m.group(2))
        rest = m.group(3).strip()
        ints = [int(x) for x in rest.split()] if rest else []
        bottom.append([[w, h], ints])

    return shapes, bottom


p = Path(__file__).with_name(file_path)
shapes, bottom = parse_shapes_and_bottom(p)

# Convert shapes dict to a list ordered by index for easier consumption
if shapes:
    max_idx = max(shapes.keys())
    shapes_list = [shapes.get(i) for i in range(max_idx + 1)]
else:
    shapes_list = []

def trim_grid(grid):
    if not grid or not grid[0]:
        return grid

    rows, cols = len(grid), len(grid[0])
    top = 0
    while top < rows and all(x == 0 for x in grid[top]):
        top += 1

    bottom = rows - 1
    while bottom >= top and all(x == 0 for x in grid[bottom]):
        bottom -= 1

    left = 0
    while left < cols and all(grid[r][left] == 0 for r in range(top, bottom + 1)):
        left += 1

    right = cols - 1
    while right >= left and all(grid[r][right] == 0 for r in range(top, bottom + 1)):
        right -= 1

    return [row[left:right + 1] for row in grid[top:bottom + 1]]

shapes_with_transforms = []
for shape in shapes_list:
    transforms = [shape]
    prev = shape
    for k in range(0, 4):
        
        transform  = []
        for j in range(len(prev[0])):
            new_row = []
            for i in range(len(prev) -1, -1, -1):
                new_row.append(prev[i][j])
            transform.append(new_row)

            flip = [row[::-1] for row in transform]

        transforms.append(transform)
        prev = transform
        transforms.append(flip)
    shapes_with_transforms.append(transforms)

for index, transforms in enumerate(shapes_with_transforms):
    seen = set()
    #trimmed_transforms = [trim_grid(transform) for transform in transforms]

    unique_transofrms = []
    for transform in transforms:
        key = tuple(tuple(row) for row in transform)
        if key not in seen:
            seen.add(key)
            unique_transofrms.append(transform)
    shapes_with_transforms[index] = unique_transofrms

for shape in shapes_with_transforms:
    for tr in shape:
        for row in tr:
            print(row)
        print("     ")
    print("----------")

def all_presents_set(score):
    return all(x == 0 for x in score)

def transofrm_valid(field):
    return all(cell < 2 for row in field for cell in row)

def add_transform(field, row, col, transform):
    valid = True
    for i in range(0, len(transform)):
        for j in range(0, len(transform[i])):
            field[row + i][col + j] += transform[i][j]
            if field[row + i][col + j] > 1:
                valid = False

    return valid

def remove_transform(field, row, col, transform):
    for i in range(0, len(transform)):
        for j in range(0, len(transform[i])):
            field[row + i][col + j] -= transform[i][j]

def solve_recursive(field, score, row, col):
    if all(s == 0 for s in score):
        return True
    
    j = col
    for i in range(row, len(field)):
        while j < len(field[0]):
            if(field[i][j]) == 1:
                j += 1
                continue
            for k in range(0, len(score)):
                if(score[k] > 0):
                    transofrms = shapes_with_transforms[k]
                    for transform in transofrms:
                        if(i + len(transform) <= len(field) and j + len(transform[0]) <= len(field[0])):
                            if add_transform(field, i, j, transform):
                                score[k] -= 1
                                if all(s == 0 for s in score):
                                    return True
                                if solve_recursive(field, score, i, j+1):
                                    return True
                                score[k] += 1
                            remove_transform(field, i, j, transform)
            j += 1
        j = 0
    return False

def create_grid(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]

res = 0
for case in bottom:
    field = create_grid(case[0][0], case[0][1])
    if(solve_recursive(field, case[1], 0, 0)):
        res+=1
    print("solved")

print(res)

