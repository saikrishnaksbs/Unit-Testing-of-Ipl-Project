'''File for '''

import unittest
from q8 import calculate

class stackedbar(unittest.TestCase):
    '''A class for '''

    def test1(self):
        '''A function for '''

        res = calculate("mock_matches.csv", "mock_deliveries.csv")
        self.assertEqual(res, {'Bipul Sharma': 0, 'Harbhajan Singh': 0, 
                               'TS Mills': 0, 'AB Dinda': 1, 'AR Patel': 1, 
                               'Sandeep Sharma': 1, 'SL Malinga': 2, 'TA Boult': 4, 
                               'Z Khan': 5})
        
    def test2(self):
        '''A function for '''

        res = calculate("mock_matches.csv", "mock_deliveries.csv")
        self.assertIsNot(res, {'Bipul Sharma': 0, 'Harbhajan Singh': 0, 
                               'TS Mills': 0, 'AB Dinda': 1, 'AR Patel': 1, 
                               'Sandeep Sharma': 1, 'SL Malinga': 2, 'TA Boult': 4, 
                               'Z Khan': 4})


if __name__ == '__main__':
    unittest.main()
