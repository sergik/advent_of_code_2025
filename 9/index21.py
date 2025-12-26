file_path = "input.txt"



with open(file_path, "r") as f:
    lines = [line.rstrip('\n') for line in f if line.rstrip('\n') != ""]



red_cords = [list(map(int,line.split(','))) for line in lines]

def range_ingersect(a_start, a_end, b_start, b_end):
    return max(a_start, b_start) < min(a_end, b_end)

def rec_intersect_polygon(rect, polygon):
    rect_x1, rect_y1 = rect[0]
    rect_x2, rect_y2 = rect[1]

    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]

        if x1 == x2:
            ymin, ymax = sorted([y1, y2])
            if rect_x1 < x1 < rect_x2:
                if range_ingersect(rect_y1, rect_y2, ymin, ymax):
                    return True
        else:
            xmin, xmax = sorted([x1, x2])
            if rect_y1 < y1 < rect_y2:
                if range_ingersect(rect_x1, rect_x2, xmin, xmax):
                    return True
    return False
EPS = 1e-12
def point_on_orth_edge(p, a, b):
    x, y = p
    x1, y1 = a
    x2, y2 = b

    # вертикальное ребро
    if x1 == x2:
        return abs(x - x1) <= EPS and min(y1, y2) - EPS <= y <= max(y1, y2) + EPS

    # горизонтальное ребро
    if y1 == y2:
        return abs(y - y1) <= EPS and min(x1, x2) - EPS <= x <= max(x1, x2) + EPS

    return False

def point_in_polygon(p, polygon):
    x, y = p

    inside = False
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]
        if point_on_orth_edge(p,  polygon[i], polygon[(i + 1) % len(polygon)]):
            return True
        if x1 == x2:
            if min(y1, y2) <= y < max(y1, y2) and x < x1:
                inside = not inside
    return inside

def get_rectangle_other_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return [(x1, y2), (x2, y1)]

max_size=0
for i in range(len(red_cords)- 1):
    for j in range(i + 1, len(red_cords)):
        point1 = red_cords[i]
        point2 = red_cords[j]
        point3, point4 = get_rectangle_other_points(point1, point2)

        rect = [point1, point2, point3, point4]
        min_point = (min(x for x, y in rect), min(y for x, y in rect))
        max_point = (max(x for x, y in rect), max(y for x, y in rect))

        if rec_intersect_polygon([min_point, max_point], red_cords):
            continue


        if  (not point_in_polygon(point3, red_cords) or not point_in_polygon(point4, red_cords)):
            continue

        size = (abs(red_cords[i][0] - red_cords[j][0]) + 1) * (1 + abs((red_cords[i][1] - red_cords[j][1])))
        max_size = max(max_size, size)

print(max_size)