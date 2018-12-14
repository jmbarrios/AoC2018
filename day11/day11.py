import sys


def cell_pl(x, y, serial_number):
    r_id = 10+x
    u = (r_id*y+serial_number)*r_id
    return ((u // 100) % 10) - 5


def create_grid_pl(serial_number):
    grid = {}
    for i in range(1, 301):
        for j in range(1, 301):
            grid[(i, j)] = cell_pl(i, j, serial_number)

    return grid


def solution1(input_sn):
    g = create_grid_pl(input_sn)
    pl = {}
    for i in range(1, 301-3):
        for j in range(1, 301-3):
            pl[(i, j)] = sum([g[(m, n)] for m in range(i, i+3)
                              for n in range(j, j+3)])

    max_sq = max(pl.keys(), key=lambda coords: pl[coords])

    return max_sq


def solution2(input_sn):
    pass


def main(input_sn, part):

    puzzle_solutions = {1: solution1,
                        2: solution2}

    solution = puzzle_solutions.get(part)

    sol = solution(input_sn)
    print(sol)


if __name__ == '__main__':
    input_sn = int(sys.argv[1])
    part = 1
    try:
        part = int(sys.argv[2])
    except IndexError:
        pass

    main(input_sn, part)
