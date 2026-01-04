import re
from pathlib import Path

file_path = "input.txt"


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
max_idx = max(shapes.keys())
shapes_list = [shapes.get(i) for i in range(max_idx + 1)]

shape_sizes = []
for shape in shapes_list:
    print(shape)
    size = 0
    for r in shape:
        for c in r:
            if c == 1:
                size+=1
    shape_sizes.append(size)

res = 0
for case in bottom:
    field_size = case[0][0]* case[0][1]
    figure_size = 0
    print(case[1])
    for i in range(len(case[1])):
        figure_size += case[1][i] * shape_sizes[i]

    if figure_size * 1.3 < field_size:
        res +=1
    elif figure_size > field_size:
        print("NOT")
    else:
        print("Hard")


print(res)

