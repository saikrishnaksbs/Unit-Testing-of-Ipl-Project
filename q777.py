'''File for '''

import unittest
from q7 import calculate

class stackedbar(unittest.TestCase):
    '''A class for '''

    def test1(self):
        '''A function for '''

        res = calculate("mock_matches.csv", "mock_deliveries.csv")
        self.assertEqual(res, {'Gujarat Lions': 3, 'Kolkata Knight Riders': 0,
                               'Mumbai Indians': 1, 'Rising Pune Supergiants': 8,
                               'Sunrisers Hyderabad': 1})
        
    def test2(self):
        '''A function for '''

        res = calculate("mock_matches.csv", "mock_deliveries.csv")
        self.assertIsNot(res, {'Gujarat Lions': 3, 'Kolkata Knight Riders': 0,
                               'Mumbai Indians': 1, 'Rising Pune Supergiants': 8,
                               'Sunrisers Hyderabad': 5})


if __name__ == '__main__':
    unittest.main()
