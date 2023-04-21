import solver_funcs


def get_cages():
    cage_count = int(input('Number of cages: '))
    cages = []
    cage_ints = []
    for cage in range(0, cage_count):
        cage_input = input('Cage number %d: ' % cage).split()
        for number in cage_input:
            cage_ints.append(int(number))
        cages.append(cage_ints)
        cage_ints = []
    return cages


def main():
    puzzle = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]
    cages = get_cages()

    row = 0
    col = 0

    checks = 0
    backtracks = 0

    while (row >= 0 and row <= 4 and
           col >= 0 and col <= 4):
        puzzle[row][col] += 1
        is_valid = solver_funcs.check_valid(puzzle, cages)
        checks += 1
        if is_valid is True:
            col += 1
            if col > 4:
                row += 1
                col = 0
        elif is_valid is False and puzzle[row][col] == 5:
            while puzzle[row][col] == 5:
                puzzle[row][col] = 0
                col -= 1
                backtracks += 1
                if col < 0:
                    row -= 1
                    col = 4

    print('\n--Solution--\n')

    for row in range(0, 5):
        for col in range(0, 5):
            print(puzzle[row][col], end=' ')
        print()

    print('\nchecks: %d backtracks: %d' % (checks, backtracks))


if __name__ == '__main__':
    main()
