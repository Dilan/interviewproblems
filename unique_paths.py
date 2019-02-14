# https://leetcode.com/problems/unique-paths/

# A robot is located at the top-left corner of a m x n grid
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid
# How many possible unique paths are there?

class Solution(object):
    def uniquePaths(self, m, n):
        mx = [[1] * n]
        for j in range(1,m):
            mx.append([0] * n)

        for j in range(1, len(mx)):
            row = mx[j]
            for i, val in enumerate(row):
                left_value = mx[j][i-1] if i-1 >= 0 else 0
                top_value = mx[j-1][i] if j-1 >= 0 else 0

                mx[j][i] = left_value + top_value

        return mx[m-1][n-1]

# CLI
if __name__ == '__main__':
    arr = [
        (3,2), (7,3),(100,100),(1000,1000)
    ]
    for data in arr:
        m,n = data
        result = Solution().uniquePaths(m,n)
        print(result)
