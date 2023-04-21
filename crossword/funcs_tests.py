import unittest

import finder_funcs

# Here is a sample puzzle you can use in your tests
puzzle = ["WAQHGTTWEE",
          "CBMIVQQELS",
          "APXWKWIIIL",
          "LDELFXPIPV",
          "PONDTMVAMN",
          "OEDSOYQGOB",
          "LGQCKGMMCT",
          "YCSLOACUZM",
          "XVDMGSXCYZ",
          "UUIUNIXFNU"]

raw_puzzle = ('WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMN' +
              'OEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU')


class TestCases(unittest.TestCase):
    def test_extract_puzzle(self):
        self.assertEqual(finder_funcs.extract_puzzle(raw_puzzle), puzzle)

    def test_search_forward_1(self):
        self.assertEqual(
            finder_funcs.search_forward(puzzle, 'UNIX'), ('FORWARD', 9, 3))

    def test_search_forward_2(self):
        self.assertEqual(
            finder_funcs.search_forward(puzzle, 'SLO'), ('FORWARD', 7, 2))

    def test_search_forward_3(self):
        self.assertEqual(
            finder_funcs.search_forward(puzzle, 'STATS'), ('FORWARD', -1, -1))

    def test_search_backward_1(self):
        self.assertEqual(
            finder_funcs.search_backward(puzzle, 'VIM'), ('BACKWARD', 1, 4))

    def test_search_backward_2(self):
        self.assertEqual(
            finder_funcs.search_backward(puzzle, 'TCMM'), ('BACKWARD', 6, 9))

    def test_search_backward_3(self):
        self.assertEqual(finder_funcs.search_backward(puzzle, 'STATS'),
                         ('BACKWARD', -1, -1))

    def test_search_down_1(self):
        self.assertEqual(
            finder_funcs.search_down(puzzle, 'CALPOLY'), ('DOWN', 1, 0))

    def test_search_down_2(self):
        self.assertEqual(
            finder_funcs.search_down(puzzle, 'LDSC'), ('DOWN', 3, 3))

    def test_search_down_3(self):
        self.assertEqual(
            finder_funcs.search_down(puzzle, 'STATS'), ('DOWN', -1, -1))

    def test_search_up_1(self):
        self.assertEqual(
            finder_funcs.search_up(puzzle, 'COMPILE'), ('UP', 6, 8))

    def test_search_up_2(self):
        self.assertEqual(
            finder_funcs.search_up(puzzle, 'CSDL'), ('UP', 6, 3))

    def test_search_up_3(self):
        self.assertEqual(
            finder_funcs.search_up(puzzle, 'STATS'), ('UP', -1, -1))

    def test_search_diagonal_1(self):
        self.assertEqual(finder_funcs.search_diagonal(puzzle, 'CPE'),
                         ('DIAGONAL', 1, 0))

    def test_search_diagonal_2(self):
        self.assertEqual(finder_funcs.search_diagonal(puzzle, 'COSX'),
                         ('DIAGONAL', 6, 3))

    def test_search_diagonal_3(self):
        self.assertEqual(finder_funcs.search_diagonal(puzzle, 'PAOT'),
                         ('DIAGONAL', 3, 6))

    def test_search_diagonal_4(self):
        self.assertEqual(finder_funcs.search_diagonal(puzzle, 'STATS'),
                         ('DIAGONAL', -1, -1))

    def test_search_all_1(self):
        self.assertEqual(
            finder_funcs.search_all(puzzle, 'CALPOLY'), ('DOWN', 1, 0))

    def test_search_all_2(self):
        self.assertFalse(finder_funcs.search_all(puzzle, 'STATS'))


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
