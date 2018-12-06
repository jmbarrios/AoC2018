import sys
from string import ascii_lowercase

def reacts(x, y):
    if x == y or x.lower() != y.lower():
        return False
    return True

def remove_reaction(chain, i):
    return chain[:i-1]+chain[i+1:]


def run_reactions(chain):
    should_continue = True
    while should_continue:
        should_continue = False
        i = 1
        while i < len(chain):
            if reacts(chain[i-1], chain[i]):
                should_continue = True
                chain = remove_reaction(chain, i)
            i += 1

    return(len(chain))


def solution1(input_file):
    with open(input_file, 'r') as f:
        chain = f.readline().strip('\n')

    should_continue = True
    while should_continue:
        should_continue = False
        i = 1
        while i < len(chain):
            if reacts(chain[i-1], chain[i]):
                should_continue = True
                chain = remove_reaction(chain, i)
            i += 1

    return(len(chain))


def solution2(input_file):
    with open(input_file, 'r') as f:
        chain = f.readline().strip('\n')

    lengths = {}
    for l in ascii_lowercase:
        new_chain = str(chain).replace(l,'').replace(l.upper(),'')
        lengths[l] = run_reactions(new_chain)

    return min(lengths.values())



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
