import unittest
from sort.quick_sort import quick_sort

class Problem_PhoneList_Test(unittest.TestCase):

    def test_01(self):
        list = [4,1,2,3,8,9,6]
        quick_sort(list)

        self.assertEqual(
            str([1,2,3,4,6,8,9]),
            str(list)
        )

if __name__ == '__main__':
    unittest.main()