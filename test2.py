'''File for testing'''

import unittest
from q2 import calculate


class MaxRuns(unittest.TestCase):
    '''A class for testing '''

    def test1(self):
        '''A function for validation '''

        res = calculate("mock_matches2.csv", "mock_deliveries2.csv")
        self.assertEqual(res, {'CH Gayle': 3, 'V Kohli': 5})                                             

    def test2(self):
        '''A function for invalidation'''

        res = calculate("mock_matches.csv", "mock_deliveries.csv")
        self.assertIsNot(res, {'Vishnu Vinod': 1,
                               'CH Gayle': 1, 'SR Watson': 5})


if __name__ == '__main__':
    unittest.main()
