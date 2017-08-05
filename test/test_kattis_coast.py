import unittest
from kattis.coast import calculate_coast_length

class Problem_Coast_Test(unittest.TestCase):

    def test_01(self):
        result = calculate_coast_length([
            "01010",
            "10101",
            "01010"
        ])
        self.assertEqual(20, result)

    def test_02(self):
        result = calculate_coast_length([
            "00011",
            "01101",
            "01001",
            "00110"
        ])
        self.assertEqual(16, result)

    def test_03(self):
        result = calculate_coast_length([
            "11111",
            "10001",
            "11111",
            "11111"
        ])
        self.assertEqual(18, result)


if __name__ == '__main__':
    unittest.main()
