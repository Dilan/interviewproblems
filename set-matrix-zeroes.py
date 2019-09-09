"""
https://leetcode.com/problems/set-matrix-zeroes/

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        y_size = len(matrix)
        x_size = len(matrix[0])

        for y in range(y_size):
            x = 0
            while(x < x_size):
                if matrix[y][x] == 0:
                    for i in range(x_size):
                        if matrix[y][i] != "#" and matrix[y][i] != 0:
                            matrix[y][i] = "#"
                    for j in range(y_size):
                        if matrix[j][x] != "#" and matrix[j][x] != 0:
                            matrix[j][x] = "#"

                x += 1

        for y in range(y_size):
            for x in range(x_size):
                if matrix[y][x] == "#":
                    matrix[y][x] = 0

def print_matrix(*args):
    boards = list(args)
    for idx, line in enumerate(boards[0]):
        s = " ".join(str(x) for x in line) + "    "
        for b in boards[1:]:
            s += " ".join(str(x) for x in b[idx]) + "\t"
        print s

if __name__ == "__main__":

    data = [
        (
            [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
            [[0,0,0,0],[0,4,5,0],[0,3,1,0]]),
    ]

    for item in data:
        m, answer = item
        Solution().setZeroes(m)
        print_matrix(m, answer)

        # print(m, answer)
