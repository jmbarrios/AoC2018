import sys
import re
import numpy as np
from collections import defaultdict, deque

def decode_str(or_str):
    return [int(c == '#') for c in or_str]


def reader(input_file):
    spread_pattern = {}
    with open(input_file, 'r') as f:
        l = f.readlines()

    input_state = decode_str(l[0].split()[2])

    for i in l[2:]:
        k = tuple(decode_str(i.split()[0]))
        v = i.split()[2]
        spread_pattern[k] = int(v == '#')

    return input_state, spread_pattern


def solution1(input_file):
    generation, spread = reader(input_file)
    next_gen = list(generation)
    offset = 0
    for g in range(20):
        generation = [0]*5+generation+[0]*5
        next_gen = [0]*5+next_gen+[0]*5
        offset += 5
        for i in range(2, len(generation)-3):
            next_gen[i] = spread[tuple(generation[i-2:i+3])]
        next_gen = np.trim_zeros(next_gen, 'f')
        offset = offset + len(next_gen) - len(generation)
        next_gen = np.trim_zeros(next_gen, 'b')
        generation = list(next_gen)

    res = [i-offset for i in range(len(generation)) if generation[i] == 1]

    return sum(res)

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
