# https://leetcode.com/problems/unique-paths/

# A robot is located at the top-left corner of a m x n grid
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid
# Now consider if some [obstacles] are added to the grids.
# How many unique paths would there be?

class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        mx  = []
        for idx, arr in enumerate(obstacleGrid):
            mx.append([0] * len(arr))

        for j in range(0, len(mx)):
            row = mx[j]
            for i, val in enumerate(row):
                if i == j and j == 0:
                    mx[j][i] = 0 if obstacleGrid[j][i] else 1
                    continue

                if obstacleGrid[j][i] == 1:
                    mx[j][i] = 0
                    continue

                left_value = mx[j][i-1] if i-1 >= 0 else 0
                top_value = mx[j-1][i] if j-1 >= 0 else 0

                mx[j][i] = left_value + top_value

        m, n = len(mx), len(mx[0])
        return mx[m-1][n-1]

if __name__ == '__main__':
    items = [
        ([
            [0,0,0],
            [0,1,0],
            [0,0,0],
        ], 2),
        ([
            [1],
        ], 0),
        ([
            [0,0,0],
            [0,0,0],
        ], 3),

    ]
    for data in items:
        grid, answer = data
        result = Solution().uniquePathsWithObstacles(grid)
        print('Answer vs Result', str(answer) + ' vs ' + str(result))
