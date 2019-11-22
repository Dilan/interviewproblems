# https://leetcode.com/problems/largest-triangle-area/submissions/

# You have a list of points in the plane. 
# Return the area of the largest triangle that can be formed by any 3 of the points.

from itertools import combinations

class Solution(object):

    @staticmethod
    def area(dots):
        x1, y1 = dots[0][0], dots[0][1]
        x2, y2 = dots[1][0], dots[1][1]
        x3, y3 = dots[2][0], dots[2][1]
        return abs(
            0.5 * ((x2*y1 + x1*y3 + x3*y2) - (x1*y2 + x3*y1 + x2*y3))
        )


    def largestTriangleArea(self, points):
        items = combinations(points, 3)

        largest_area = 0.0
        for p in items:
            largest_area = max(self.area(p), largest_area)

        return largest_area


if __name__ == '__main__':

    data = [
        ([[0,0],[0,1],[1,0],[0,2],[2,0]], 2.0),
        ([[1,0],[0,0],[0,1]], 0.5),
    ]

    for item in data:
        points, answer = item
        result = Solution().largestTriangleArea(points)
        print(result, 'vs'm answer)
