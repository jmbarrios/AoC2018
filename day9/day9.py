import sys
import re
from collections import defaultdict, deque


def solution1(input_file):
    with open(input_file, 'r') as f:
        l = f.readline()
        no_of_players, no_of_marbles = map(int, re.findall(r'[0-9]+', l))

    player_score = defaultdict(int)
    circle = deque([0])
    current_player = 0
    for m in range(1, no_of_marbles+1):
        current_player = (current_player + 1) % no_of_players
        if m % 23 == 0:
            circle.rotate(7)
            player_score[current_player] += m + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(m)

    return max(player_score.values())


def solution2(input_file):
    with open(input_file, 'r') as f:
        l = f.readline()
        no_of_players, no_of_marbles = map(int, re.findall(r'[0-9]+', l))

    no_of_marbles = no_of_marbles * 100
    player_score = defaultdict(int)
    circle = deque([0])
    current_player = 0
    for m in range(1, no_of_marbles+1):
        current_player = (current_player + 1) % no_of_players
        if m % 23 == 0:
            circle.rotate(7)
            player_score[current_player] += m + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(m)

    return max(player_score.values())


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
