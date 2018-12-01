import sys


def solution1(input_file):
    sum = 0
    with open(input_file, 'r') as f:
        for line in f:
            sum += int(line)

    return sum


def solution2(input_file):
    sum = 0
    visited = {0}

    with open(input_file, 'r') as f:
        freq = f.readlines()
        freq = map(int, freq)

    while True:
        for el in freq:
            sum += el
            if (sum in visited):
                return sum

            visited.add(sum)


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

