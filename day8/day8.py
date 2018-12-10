import sys
import re


def parse_data(data):
    childrens, metadata = data[:2]
    data_remain = data[2:]
    sum_meta = 0
    values = []

    for children in range(childrens):
        sum_m, value, data_remain = parse_data(data_remain)
        sum_meta += sum_m
        values.append(value)


    sum_meta += sum(data_remain[:metadata])
    if childrens == 0:
        return (sum_meta,
                sum(data_remain[:metadata]),
                data_remain[metadata:])
    else:
        return (sum_meta,
                sum([values[k-1]
                    for k in data_remain[:metadata] if k > 0
                    and k <= len(values)]),
                data_remain[metadata:])


def solution1(input_file):
    with open(input_file, 'r') as f:
        data = f.readline().strip('\n')
        data = map(int, data.split())

    sum_m, _, _ = parse_data(data)
    return sum_m

def solution2(input_file):
    with open(input_file, 'r') as f:
        data = f.readline().strip('\n')
        data = map(int, data.split())

    _, sum_root, _ = parse_data(data)
    return sum_root


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
