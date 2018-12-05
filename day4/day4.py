import sys
from collections import defaultdict


def get_minutes(r):
    return int(r.split()[1].split(':')[1].strip('\]'))


def get_guard(r):
    return int(r.split()[3].strip('#'))


def most_frequent_guard_minute(d):
    best = None
    for k, v in d.items():
        if best is None or v > d[best]:
            best = k

    return best


def solution1(input_file):
    with open(input_file, 'r') as f:
        input_log = f.readlines()

    input_log.sort()
    total_sleep_time = defaultdict(int)
    sleep_by_minute = defaultdict(int)
    guard_id = None
    time = None
    for l in input_log:
        curr_time = get_minutes(l)
        if 'Guard' in l:
            guard_id = get_guard(l)
        elif 'falls asleep' in l:
            time = get_minutes(l)
        elif 'wakes up' in l:
            for ms in range(time, curr_time):
                sleep_by_minute[(guard_id, ms)] += 1
                total_sleep_time[guard_id] += 1

    choosen_guard = max(total_sleep_time.keys(),
                        key=lambda guard_id: total_sleep_time[guard_id])

    guard_sleep_pattern = {k[1]: v for k, v in
                           sleep_by_minute.items() if k[0] == choosen_guard}

    choosen_min = max(guard_sleep_pattern.keys(),
                      key=lambda minute: guard_sleep_pattern[minute])

    print(choosen_min)
    print(choosen_guard)
    return choosen_guard * choosen_min


def solution2(input_file):
    with open(input_file, 'r') as f:
        input_log = f.readlines()

    input_log.sort()
    sleep_by_minute = defaultdict(int)
    guard_id = None
    time = None
    for l in input_log:
        curr_time = get_minutes(l)
        if 'Guard' in l:
            guard_id = get_guard(l)
        elif 'falls asleep' in l:
            time = get_minutes(l)
        elif 'wakes up' in l:
            for ms in range(time, curr_time):
                sleep_by_minute[(guard_id, ms)] += 1

    choosen_guard, choosen_min = most_frequent_guard_minute(sleep_by_minute)

    print(choosen_min)
    print(choosen_guard)
    return choosen_guard * choosen_min


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
