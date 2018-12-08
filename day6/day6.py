import sys
import math
from collections import Counter


def distance(x, y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])


def solution1(input_file):
    centers = []
    with open(input_file, 'r') as f:
        for l in f:
            c = l.strip('\n').split(', ')
            c = [int(i) for i in c]
            centers.append(tuple(c))

    max_x = max([x[0] for x in centers])
    max_y = max([x[1] for x in centers])
    grid = {}
    for i in range(max_x):
        for j in range(max_y):
            min_dis = min(distance(c, (i, j)) for c in centers)
            for n, c in enumerate(centers):
                if distance(c, (i,j)) == min_dis:
                    if grid.get((i, j), -1) != -1:
                         grid[(i, j)] = -1
                         break
                    grid[(i, j)] = n

    frontier_centers = set([-1])
    frontier_centers = frontier_centers.union(
            set([grid[(x, max_y-1)] for x in range(max_x)]))
    frontier_centers = frontier_centers.union(
            set(grid[(x, 0)] for x in range(max_x)))
    frontier_centers = frontier_centers.union(
            set(grid[(max_x-1, y)] for y in range(max_y)))
    frontier_centers = frontier_centers.union(
            set(grid[(0, y)] for y in range(max_y)))

    return next(cluster[1] for cluster in
                Counter(grid.values()).most_common()
                if cluster[0] not in frontier_centers)


def solution2(input_file):
    centers = []
    with open(input_file, 'r') as f:
        for l in f:
            c = l.strip('\n').split(', ')
            c = [int(i) for i in c]
            centers.append(tuple(c))

    max_x = max([x[0] for x in centers])
    max_y = max([x[1] for x in centers])
    grid = {}
    for i in range(max_x):
        for j in range(max_y):
            reachable = 1 if sum([distance(c, (i,j)) for c in centers]) < 10000 else -1
            grid[(i, j)] = reachable

    return len([e for e in grid.values() if e == 1])


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
