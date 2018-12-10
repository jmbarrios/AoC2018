import sys
import re


def solution1(input_file):
    tasks = {}
    my_re = r'[A-Z]'
    with open(input_file, 'r') as f:
        for l in f:
            _, b, a = re.findall(my_re, l)
            if b:
                if a not in tasks:
                    tasks[a] = []
                if b not in tasks:
                    tasks[b] = []
                tasks[a].append(b)

    tasks = sorted(tasks.items(), key=lambda t: t[0])

    done_ord = []
    done = set()
    while len(done) != len(tasks):
        for after, before in tasks:
            if after not in done and all(t in done for t in before):
                done_ord.append(after)
                done.add(after)
                break

    return "".join(done_ord)


def solution2(input_file):
    pass


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
