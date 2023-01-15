'''File for '''

import unittest
from eq4 import calculate


class stackedbar(unittest.TestCase):
    '''A class for '''

    def test1(self):
        '''A function for '''

        res = calculate("mock_matches.csv", "mock_deliveries.csv")
        self.assertEqual(res, [['2015', '2016'], [[2, 1], [2, 1], [2, 1], [2, 2], [3, 2], [3, 0], [3, 1], [3, 1]]])


if __name__ == '__main__':
    unittest.main()
