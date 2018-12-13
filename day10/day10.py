import sys
import re


class Point():
    def __init__(self, x, y, dx, dy):
        self.x = int(x)
        self.y = int(y)
        self.dx = int(dx)
        self.dy = int(dy)

    def __str__(self):
        return 'pos: {} {}, vel: {}, {}'.format(self.x,
                                                self.y,
                                                self.dx,
                                                self.dy)

    def tick(self):
        self.x += self.dx
        self.y += self.dy


def move(list_of_points):
    for p in list_of_points:
        p.tick()


def get_bbox(list_of_points):
    l = min(p.x for p in list_of_points)
    r = max(p.x for p in list_of_points)
    b = min(p.y for p in list_of_points)
    t = max(p.y for p in list_of_points)

    return l, r, b, t


def in_bounds(list_of_points):
    l, r, b, t = get_bbox(list_of_points)

    dif_x = abs(r - l)
    dif_y = abs(t - b)
    s = 200

    if dif_x < s and dif_y < s:
        return True
    else:
        return False


def vis_positions(list_of_points):
    l, r, b, t = get_bbox(list_of_points)
    out = ''
    for y in range(b, t+1):
        for x in range(l, r+1):
            if (x, y) in [(p.x, p.y) for p in list_of_points]:
                out += '#'
            else:
                out += '.'
        out += '\n'

    return out


def solution1(input_file):
    coordinates_re = r'-?[0-9]+'
    points = []
    with open(input_file, 'r') as f:
        for line in f:
            p = re.findall(coordinates_re, line)
            p = Point(*p)
            points.append(p)

    print(len(points))
    out = None
    for i in range(100000):
        move(points)

        if in_bounds(points):
            o = vis_positions(points)
            if out is None or len(o) < len(out):
                # Choose minimal len value
                out = o

    return out


def solution2(input_file):
    coordinates_re = r'-?[0-9]+'
    points = []
    with open(input_file, 'r') as f:
        for line in f:
            p = re.findall(coordinates_re, line)
            p = Point(*p)
            points.append(p)

    print(len(points))
    out = None
    for i in range(100000):
        move(points)

        if in_bounds(points):
            o = vis_positions(points)
            if out is None or len(o) < len(out):
                # Choose minimal len value
                out = o
                eta = i + 1

    return eta


def main(input_file, part):

    puzzle_solutions = {1: solution1,
                        2: solution2}

    solution = puzzle_solutions.get(part)

    sol = solution(input_file)
    print(sol)


if __name__ == '__main__':
    input_file = sys.argv[1]
    part = 1
    try:
        part = int(sys.argv[2])
    except IndexError:
        pass

    main(input_file, part)

