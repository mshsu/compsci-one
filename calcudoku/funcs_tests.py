import unittest

import solver_funcs


class TestCases(unittest.TestCase):
    def test_check_valid_with_finished_puzzle(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertTrue(solver_funcs.check_valid(puzzle, cages))

    def test_check_valid1(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 0, 0, 0]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertTrue(solver_funcs.check_valid(puzzle, cages))

    def test_check_valid2(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 5, 1, 4]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertFalse(solver_funcs.check_valid(puzzle, cages))

    def test_check_valid3(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 5, 3, 2],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertFalse(solver_funcs.check_valid(puzzle, cages))

    def test_check_valid4(self):
        puzzle = [[1, 2, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertTrue(solver_funcs.check_valid(puzzle, cages))

    def test_check_cages_valid1(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertTrue(solver_funcs.check_cages_valid(puzzle, cages))

    def test_check_cages_valid2(self):
        puzzle = [[4, 5, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertFalse(solver_funcs.check_cages_valid(puzzle, cages))

    def test_check_cages_valid3(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 1, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertFalse(solver_funcs.check_cages_valid(puzzle, cages))

    def test_check_cages_valid4(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [0, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertTrue(solver_funcs.check_cages_valid(puzzle, cages))

    def test_check_cages_valid5(self):
        puzzle = [[5, 1, 2, 5, 3],
                  [0, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertFalse(solver_funcs.check_cages_valid(puzzle, cages))

    def test_check_cages_valid6(self):
        puzzle = [[4, 5, 0, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertFalse(solver_funcs.check_cages_valid(puzzle, cages))

    def test_check_cage_full1(self):
        puzzle = [[0, 1, 1, 0, 0],
                  [0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertTrue(solver_funcs.check_cage_full(puzzle, cages, 1))

    def test_check_cage_full2(self):
        puzzle = [[0, 1, 0, 0, 0],
                  [0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertFalse(solver_funcs.check_cage_full(puzzle, cages, 1))

    def test_check_cage_sum1(self):
        puzzle = [[0, 1, 2, 0, 0],
                  [0, 5, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertEqual(solver_funcs.check_cage_sum(puzzle, cages, 1), 8)

    def test_check_cage_sum2(self):
        puzzle = [[1, 0, 0, 0, 0],
                  [4, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertEqual(solver_funcs.check_cage_sum(puzzle, cages, 0), 5)

    def test_check_cage_sum3(self):
        puzzle = [[0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 3, 0, 0, 0],
                  [0, 4, 0, 0, 0],
                  [5, 2, 0, 0, 0]]

        cages = [[5, 2, 0, 5],
                 [8, 3, 1, 2, 6],
                 [8, 2, 3, 8],
                 [6, 3, 4, 9, 14],
                 [13, 3, 7, 12, 13],
                 [5, 2, 10, 15],
                 [14, 4, 11, 16, 20, 21],
                 [6, 3, 17, 18, 22],
                 [10, 3, 19, 23, 24]]

        self.assertEqual(solver_funcs.check_cage_sum(puzzle, cages, 6), 14)

    def test_check_columns_valid1(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 1, 4, 3, 2],
                  [2, 1, 5, 4, 1],
                  [3, 1, 1, 2, 5],
                  [5, 1, 3, 1, 4]]

        self.assertFalse(solver_funcs.check_columns_valid(puzzle))

    def test_check_columns_valid2(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        self.assertTrue(solver_funcs.check_columns_valid(puzzle))

    def test_check_columns_valid3(self):
        puzzle = [[4, 0, 2, 5, 3],
                  [1, 0, 4, 3, 2],
                  [2, 0, 5, 4, 1],
                  [3, 0, 1, 2, 5],
                  [5, 0, 3, 1, 4]]

        self.assertTrue(solver_funcs.check_rows_valid(puzzle))

    def test_check_rows_valid1(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [1, 1, 1, 1, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        self.assertFalse(solver_funcs.check_rows_valid(puzzle))

    def test_check_rows_valid2(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [2, 3, 5, 4, 1],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        self.assertTrue(solver_funcs.check_rows_valid(puzzle))

    def test_check_rows_valid3(self):
        puzzle = [[4, 1, 2, 5, 3],
                  [1, 5, 4, 3, 2],
                  [0, 0, 0, 0, 0],
                  [3, 4, 1, 2, 5],
                  [5, 2, 3, 1, 4]]

        self.assertTrue(solver_funcs.check_rows_valid(puzzle))


if __name__ == '__main__':
    unittest.main()
