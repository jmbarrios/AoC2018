import sys
import re
from collections import defaultdict


def solution1(input_file):
    with open(input_file, 'r') as f:
        l = f.readline()
        no_of_players, no_of_marbles = map(int, re.findall(r'[0-9]+', l))

    player_score = defaultdict(int)
    circle = [0, 1]
    current_marble = 1
    current_player = 1
    for m in range(2, no_of_marbles+1):
        current_player = (current_player + 1) % no_of_players
        if m % 23 == 0:
            current_marble = (current_marble - 7) % len(circle)
            player_score[current_player] += m + circle.pop(current_marble)
        else:
            current_marble = (current_marble + 2) % len(circle)

            if current_marble == 0 and m % 23 !=0:
                current_marble = len(circle)
                circle.append(current_marble)
            else:
                circle.insert(current_marble, m)

    print(player_score)
    return max(player_score.values())


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
