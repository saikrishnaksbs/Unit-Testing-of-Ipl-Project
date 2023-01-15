'''File for '''

import unittest
from q2 import calculate


class max_runs_1(unittest.TestCase):
    '''A class for '''
    def test1(self):
        '''A function for '''

        res = calculate("mock_matches.csv", "mock_deliveries.csv")
        self.assertEqual(res, {'Vishnu Vinod': 0, 'AB de Villiers': 2,
                               'CH Gayle': 2, 'SR Watson': 5, 'V Kohli': 8})

    def test2(self):
        '''A function for '''

        res = calculate("mock_matches.csv", "mock_deliveries.csv")
        self.assertIsNot(res, {'Vishnu Vinod': 1,
                               'CH Gayle': 1, 'SR Watson': 5})


if __name__ == '__main__':
    unittest.main()
