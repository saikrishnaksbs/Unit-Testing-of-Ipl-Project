'''File for testing'''

import unittest
from q8 import calculate


class StackedBar(unittest.TestCase):
    '''A class for '''

    def test1(self):
        '''A function for '''

        res = calculate("mock_matches2.csv", "mock_deliveries2.csv")
        self.assertEqual(res, {'TA Boult': 4, 'TS Mills': 7, 'AB Dinda': 10})

    def test2(self):
        '''A function for '''

        res = calculate("mock_matches.csv", "mock_deliveries.csv")
        self.assertIsNot(res, {'TA Boult': 4, 'TS Mills': 7, 'AB Dinda': 16})


if __name__ == '__main__':
    unittest.main()
