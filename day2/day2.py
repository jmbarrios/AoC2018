import sys


def replace_i_char(s, idx):
    return s[:idx] + s[(idx+1):]


def solution1(input_file):
    count_2 = 0
    count_3 = 0

    with open(input_file, 'r') as f:
        for id in f:
            count_letters = {}
            for l in id.strip('\n'):
                cnt = count_letters.get(l, 0)
                cnt += 1
                count_letters.update({l: cnt})
            if 2 in count_letters.values():
                count_2 += 1
            if 3 in count_letters.values():
                count_3 += 1

    return count_2 * count_3



def solution2(input_file):
    with open(input_file, 'r') as f:
        ids = f.readlines()

    total_ids = len(ids)
    for i in range(total_ids):
        for j in range(i, total_ids):
            w1 = ids[i].strip('\n')
            w2 = ids[j].strip('\n')

            id = w1
            d = 0
            for k in range(len(w1)):
                if w1[k] != w2[k]:
                    d += 1
                    id = replace_i_char(id, k)

            if d == 1:
                return 'ID: {}'.format(id)



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

