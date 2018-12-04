import sys
import re
from collections import defaultdict


def get_patch_data(s):
    parse_patch = r'#(?P<id>[0-9]+)\s@\s(?P<h>[0-9]+),(?P<v>[0-9]+):\s(?P<dx>[0-9]+)x(?P<dy>[0-9]+)'

    m = re.match(parse_patch, s)
    return m.groupdict()


def solution1(input_file):
    data = []
    with open(input_file, 'r') as f:
        for line in f:
            data_it = {k: int(v) for k, v in
                       get_patch_data(line).items()}
            data.append(data_it)

    squares = defaultdict(list)
    for claim in data:
        for i in range(claim['h'],
                claim['h']+claim['dx']):
            for j in range(claim['v'],
                    claim['v']+claim['dy']):
                    squares[(i, j)].append(claim['id'])

    intersected = [1 for k, v in squares.items() if len(v)>1]

    return sum([1 for k, v in squares.items() if len(v)>1])


def solution2(input_file):
    data = []
    with open(input_file, 'r') as f:
        for line in f:
            data_it = {k: int(v) for k, v in
                       get_patch_data(line).items()}
            data.append(data_it)

    squares = defaultdict(list)
    for claim in data:
        for i in range(claim['h'],
                claim['h']+claim['dx']):
            for j in range(claim['v'],
                    claim['v']+claim['dy']):
                    squares[(i, j)].append(claim['id'])

    unique_claims = set(claim['id'] for claim in data)
    overlapping_claims = set()
    for k, v in squares.items():
        if len(v) > 1:
            for i in v:
                overlapping_claims.add(i)

    return unique_claims - overlapping_claims


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

