# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

class Solution(object):
    def isToeplitzMatrix(self, matrix):

        m = len(matrix)    # columns
        n = len(matrix[0]) # rows

        y, x = m - 1, 0
        while y < m and x < n:
            dy, dx = (y + 1, x + 1) # diagonal
            while dy < m and dx < n:
                if matrix[y][x] != matrix[dy][dx]:
                    return False
                dy, dx = dy + 1, dx + 1

            if y == 0:
                x += 1
            if y > 0:
                y -= 1

        return True

if __name__ == '__main__':
    data = [
        ([
            [11,74,0,93],
            [40,11,74,7]
        ], False),
        ([
          [1,2,3,4],
          [5,1,2,3],
          [9,5,1,2]
        ], True)
    ]

    for item in data:
        matrix, answer = item
        result = Solution().isToeplitzMatrix(matrix)

        print(result, answer)
