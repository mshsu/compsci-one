# Put your functions in here.
# Feel free to run your design past me before beginning to implement.


def extract_puzzle(raw_puzzle):
    # Makes a list of lists, where each list is a puzzle row
    puzzle = []
    for i in range(10):
        puzzle.append(raw_puzzle[(i * 10):(i * 10 + 10)])
    return puzzle


def search_forward(puzzle, word):
    row_found = -1
    col_found = -1
    for row in range(len(puzzle)):
        if puzzle[row].find(word) != -1:
            row_found = row
            col_found = puzzle[row].find(word)
    return ('FORWARD', row_found, col_found)


def make_backward(puzzle):
    # Makes a list of lists, where each list is a reversed puzzle row/col
    back_list = []
    reverse_row = []
    for row in puzzle:
        for i in range(len(row) - 1, -1, -1):
            reverse_row.append(row[i])
        back_list.append(''.join(reverse_row))
        reverse_row = []
    return back_list


def search_backward(puzzle, word):
    back_list = make_backward(puzzle)
    row_found = -1
    col_found = -1
    for row in range(len(back_list)):
        if back_list[row].find(word) != -1:
            row_found = row
            col_found = 9 - back_list[row].find(word)
    return ('BACKWARD', row_found, col_found)


def make_down(puzzle):
    # Makes a list of lists, where each list is a puzzle col
    down_list = []
    col = []
    for i in range(10):
        for row in puzzle:
            col.append(row[i])
        down_list.append(''.join(col))
        col = []
    return down_list


def search_down(puzzle, word):
    down_list = make_down(puzzle)
    row_found = -1
    col_found = -1
    for col in range(len(down_list)):
        if down_list[col].find(word) != -1:
            col_found = col
            row_found = down_list[col].find(word)
    return ('DOWN', row_found, col_found)


def search_up(puzzle, word):
    up_list = make_backward(make_down(puzzle))
    row_found = -1
    col_found = -1
    for col in range(len(up_list)):
        if up_list[col].find(word) != -1:
            col_found = col
            row_found = 9 - up_list[col].find(word)
    return ('UP', row_found, col_found)


def search_diagonal(puzzle, word):
    # 1. Search for first letter of word by row, by col
    # 2. If first letter matches and word might fit in puzzle,
    # scans diagonally for the same length of the target word
    # 3. If this word matches the target word, then it is diagonal
    # 4. If not, repeat 1-3
    # 5. If no matches, return row and col as -1
    word_candidate = []
    row_found = -1
    col_found = -1
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if (puzzle[row][col] == word[0] and
                    col <= 10 - len(word) and
                    row <= 10 - len(word)):
                for i in range(len(word)):
                    word_candidate.append(puzzle[row + i][col + i])
                if ''.join(word_candidate) == word:
                    row_found = row
                    col_found = col
                word_candidate = []
    return ('DIAGONAL', row_found, col_found)


def search_all(puzzle, word):
    results = []
    found = False

    results.append(search_forward(puzzle, word))
    results.append(search_backward(puzzle, word))
    results.append(search_up(puzzle, word))
    results.append(search_down(puzzle, word))
    results.append(search_diagonal(puzzle, word))

    for result in results:
        if result[1] != -1 and result[2] != -1:
            found = result
    return found
