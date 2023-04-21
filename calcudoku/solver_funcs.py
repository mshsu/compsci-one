
def check_valid(puzzle, cages):
    return (check_cages_valid(puzzle, cages) and
            check_columns_valid(puzzle) and
            check_rows_valid(puzzle))


def check_cages_valid(puzzle, cages):
    for cage in range(0, len(cages)):
        is_cage_full = check_cage_full(puzzle, cages, cage)
        cage_sum = check_cage_sum(puzzle, cages, cage)
        cage_target = cages[cage][0]
        if is_cage_full is True and cage_sum != cage_target:
            return False
        elif is_cage_full is False and cage_sum >= cage_target:
            return False

    return True


def check_cage_full(puzzle, cages, cage_num):
    # cage size = cages[x][1]
    # row = cages[x][y] // 5
    # column = cages[x][y] % 5
    cage_size = cages[cage_num][1]
    row = 0
    col = 0
    cage_contents = []
    for box in range(2, cage_size + 2):
        row = cages[cage_num][box] // 5
        col = cages[cage_num][box] % 5
        cage_contents.append(puzzle[row][col])
    if cage_contents.count(0) > 0:
        return False
    else:
        return True


def check_cage_sum(puzzle, cages, cage_num):
    cage_sum = 0
    cage_size = cages[cage_num][1]
    row = 0
    col = 0
    for box in range(2, cage_size + 2):
        row = cages[cage_num][box] // 5
        col = cages[cage_num][box] % 5
        cage_sum += puzzle[row][col]
    return cage_sum


def check_columns_valid(puzzle):
    # Create new list of lists where each row in list is column, not row
    # Then call check_rows_Valid
    col_matrix = []
    col_matrix_row = []
    for col in range(0, 5):
        for row in range(0, 5):
            col_matrix_row.append(puzzle[row][col])
        col_matrix.append(col_matrix_row)
        col_matrix_row = []
    return check_rows_valid(col_matrix)


def check_rows_valid(puzzle):
    row = 0
    value = 1
    value_count = 0
    while row <= 4 and value_count <= 1:
        while value <= 5 and value_count <= 1:
            value_count = puzzle[row].count(value)
            value += 1
        row += 1
        value = 1
    if value_count > 1:
        return False
    else:
        return True
