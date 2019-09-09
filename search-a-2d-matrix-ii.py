"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        y_size = len(matrix)
        x_size = len(matrix[0])

        for line in matrix:
            if line[0] <= target and line[x_size-1] >= target:
                if self.binarySearch(target, line, (0, len(line)-1)) != -1:
                    return True

        return False

    def binarySearch(self, val, arr, limits):

        low, high = limits
        pivot = int((low + high) / 2)

        if val == arr[pivot]:
            return pivot

        if high < low:
            return -1

        if arr[pivot] > val:
            high = (pivot - 1)
        if arr[pivot] < val:
            low = pivot + 1

        return self.binarySearch(val, arr, (low, high))

if __name__ == '__main__':
    data = [
        ([
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ], 5, True)
    ]

    for item in data:

        matrix, val, answer = item
        result = Solution().searchMatrix(matrix, val)

        print(result, answer)
