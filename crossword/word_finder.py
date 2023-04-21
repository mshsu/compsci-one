import finder_funcs


def main():
    puzzle = finder_funcs.extract_puzzle(input())
    words = input().split()

    print("Puzzle:\n")
    for row in puzzle:
        print(row)
    print()

    for word in words:
        result = finder_funcs.search_all(puzzle, word)
        if result is False:
            print('%s: word not found' % word)
        else:
            print('%s: (%s) row: %d column: %d' % (word, result[0],
                                                   result[1], result[2]))


if __name__ == '__main__':
    main()
