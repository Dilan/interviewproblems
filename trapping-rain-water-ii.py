# https://leetcode.com/problems/trapping-rain-water-ii
# Given an m x n matrix of positive integers representing the height of each unit
# cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

class Solution:

    def neighbors(self, x, y):
        result = []
        conditions = [
            lambda x,y: (x+1,y),
            lambda x,y: (x-1,y),
            lambda x,y: (x,y+1),
            lambda x,y: (x,y-1)
        ]
        for xy in conditions:
            x0, y0 = xy(x,y)
            if x0 >= 0 and x0 < self.size_x and y0 >= 0 and y0 < self.size_y:
                result.append((x0,y0))
        return result

    def add_to_sorted_queue(self, arr, x, y):
        value = self.heightMap[y][x]
        index = None
        for idx, v in enumerate(arr):
            if v[0] > value:
                arr.insert(idx, (value, (x,y)))
                index = idx
                break

        if index is None:
            arr.insert(len(arr), (value, (x,y)))

    def trapRainWater(self, heightMap):
        if len(heightMap) == 0:
            return 0

        self.size_y = size_y = len(heightMap)
        self.size_x = size_x = len(heightMap[0])
        self.heightMap = heightMap

        # status: 2 - visited, 1 - queued, 0 - none
        self.statusMap = []
        for j in range(self.size_y):
            self.statusMap.append([0] * self.size_x)

        queue = []
        for y in range(0,size_y):
            for x in range(0,size_x):
                if y == 0 or y == (self.size_y-1) or x == 0 or x == (self.size_x-1):
                    queue.append((heightMap[y][x], (x,y)))
                    self.statusMap[y][x] = 1
        # sort
        queue = sorted(queue)

        max_height = 0
        drops = 0
        while(len(queue)):
            value, xy = queue.pop(0)
            x,y = xy
            self.statusMap[y][x] = 2

            if value >= max_height:
                max_height = value

            for neighbor in self.neighbors(x, y):
                xN, yN = neighbor
                if self.statusMap[yN][xN] == 0:
                    if max_height > self.heightMap[yN][xN]:
                        drops += max_height - self.heightMap[yN][xN]

                    self.add_to_sorted_queue(queue, xN, yN)
                    self.statusMap[yN][xN] = 1

        return drops

heightMap = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
result = Solution().trapRainWater(heightMap)
print('Answer: ' + str(result))
