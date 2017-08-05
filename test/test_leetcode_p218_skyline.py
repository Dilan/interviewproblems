import unittest
from leetcode.problem218_skyline import skyline

class Problem_Leetcode_Skyline_Test(unittest.TestCase):

    def test_01(self):
        self.assertEqual(
            [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]],
            skyline([[ 2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
        )

if __name__ == '__main__':
    unittest.main()
