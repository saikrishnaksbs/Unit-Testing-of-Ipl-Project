'''File for testing'''

import unittest
from q4 import calculate


class StackedBar(unittest.TestCase):
    '''A class for '''

    def test1(self):
        '''A function for '''

        res = calculate("mock_matches2.csv")
        self.assertEqual(res, {'2015': {'Sunrisers Hyderabad': 1,
                                        'Royal Challengers Bangalore': 1,
                                        'Mumbai Indians': 1,
                                        'Rising Pune Supergiant': 1,
                                        'Gujarat Lions': 1,
                                        'Kolkata Knight Riders': 1,
                                        'Delhi Daredevils': 0,
                                        'Kings XI Punjab': 0},
                               '2016': {'Mumbai Indians': 1,
                                        'Rising Pune Supergiants': 1,
                                        'Delhi Daredevils': 1,
                                        'Kolkata Knight Riders': 1,
                                        'Kings XI Punjab': 1,
                                        'Gujarat Lions': 1,
                                        'Royal Challengers Bangalore': 1,
                                        'Sunrisers Hyderabad': 1}})


if __name__ == '__main__':
    unittest.main()
