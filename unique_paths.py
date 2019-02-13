# https://leetcode.com/problems/unique-paths/

# A robot is located at the top-left corner of a m x n grid
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid
# How many possible unique paths are there?

class Solution(object):
    def uniquePaths(self, m, n):
        mx = [] # init each node by (value, inputs, visited)
        for j in range(n):
            if j == 0:
                mx.append([(0,1,0)] * m)
                mx[0][0] = (1,0,-1)
            else:
                mx.append([(0,2,0)] * m)
                mx[j][0] = (0,1,0)

        # start DFS for (0,0)
        Solution.dfs(mx, 0, 0, 0)
        
        return mx[n-1][m-1][0]

    @staticmethod
    def dfs(mx, x, y, val):
        value, inputs, visited = mx[y][x]
        mx[y][x] = (value+val, inputs, visited+1)

        value, inputs, visited = mx[y][x]
        if inputs == visited:
            movements = Solution.movements(mx, x, y)
            for move in movements:
                i, j = move(x, y)
                Solution.dfs(mx, i, j, value)

    @staticmethod
    def movements(mx, x, y):
        arr = []
        if x+1 < len(mx[0]):
            arr.append(Solution.right)
        if y+1 < len(mx):
            arr.append(Solution.down)
        return arr

    @staticmethod
    def right(x,y):
        return (x+1,y)
    @staticmethod
    def down(x,y):
        return (x,y+1)

# CLI
if __name__ == '__main__':
    arr = [
        (3,2), (7,3),
    ]
    for data in arr:
        m,n = data
        result = Solution().uniquePaths(m,n)
        print(result)
