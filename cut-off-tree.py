"""
https://leetcode.com/problems/cut-off-trees-for-golf-event/

You are asked to cut off trees in a forest for a golf event.
The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through,
and this positive number represents the tree's height.


You are asked to cut off all the trees in this forest in the order of tree's height
- always cut off the tree with lowest height first.
And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need
to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs
to be cut off.
"""

class Solution(object):

    def neighbors(self, point, grid):
        # direction vector (North, South, East, West)
        dy = [-1, +1,  0,  0] # direction [rows]
        dx = [ 0,  0, -1, +1] # direction [columns]

        items = []
        x, y = point
        y_size, x_size = len(grid), len(grid[0])

        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y

            if xx >= 0 and yy >= 0 and xx < x_size and yy < y_size:
                items.append((xx,yy))

        return items

    def bfs(self, start, stop, grid):
        if start[0] == stop[0] and start[1] == stop[1]:
            return 0

        x,y = start
        visited = self.empty_grid(grid)
        queue = [(x,y,0)] # (x, y, length)

        while len(queue):
            xx,yy,length = queue.pop(0)
            visited[yy][xx] = 1

            for n in self.neighbors((xx,yy), grid):
                nx, ny = n

                if nx == stop[0] and ny == stop[1]:
                    return length + 1

                if grid[ny][nx] > 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 2
                    queue.append((nx,ny,length+1))

        return -1

    def empty_grid(self, grid):
        x_size, m = len(grid[0]), []
        for i in grid:
            line = [0] * x_size
            m.append(line)
        return m

    def cutOffTree(self, forest):
        # found all trees:
        trees = []
        for y,line in enumerate(forest):
            for x,val in enumerate(line):
                if val > 1:
                    trees.append((val,x,y))
        trees.sort(key=lambda tup: tup[0])

        # BFS for each tree
        length, start = 0, (0,0)
        while len(trees):
            val,x,y = trees.pop(0)
            l = self.bfs(start, (x,y), forest)

            if l == -1:
                return -1

            length += l
            start = (x,y)

        return length

if __name__ == "__main__":

    data = [
        ([
             [1,2,3],
             [0,0,4],
             [7,6,5]
         ], 6),
        ([
            [2,3,4],
            [0,0,5],
            [8,7,6]
        ], 6),
        ([
            [1,2,3],
            [0,0,0],
            [7,6,5]],
        -1),
        ([
            [54581641,64080174,24346381,69107959],
            [86374198,61363882,68783324,79706116],
            [668150,92178815,89819108,94701471],
            [83920491,22724204,46281641,47531096],
            [89078499,18904913,25462145,60813308]],
        57),
        ([
            [69438,55243,0,43779,5241,93591,73380],
            [847,49990,53242,21837,89404,63929,48214],
            [90332,49751,0,3088,16374,70121,25385],
            [14694,4338,87873,86281,5204,84169,5024],
            [31711,47313,1885,28332,11646,42583,31460],
            [59845,94855,29286,53221,9803,41305,60749],
            [95077,50343,27947,92852,0,0,19731],
            [86158,63553,56822,90251,0,23826,17478],
            [60387,23279,78048,78835,5310,99720,0],
            [74799,48845,60658,29773,96129,90443,14391],
            [65448,63358,78089,93914,7931,68804,72633],
            [93431,90868,55280,30860,59354,62083,47669],
            [81064,93220,22386,22341,95485,20696,13436],
            [50083,0,89399,43882,0,13593,27847],
            [0,12256,33652,69301,73395,93440,0],
            [42818,87197,81249,33936,7027,5744,64710],
            [35843,0,99746,52442,17494,49407,63016],
            [86042,44524,0,0,26787,97651,28572],
            [54183,83466,96754,89861,84143,13413,72921],
            [89405,52305,39907,27366,14603,0,14104],
            [70909,61104,70236,30365,0,30944,98378],
            [20124,87188,6515,98319,78146,99325,88919],
            [89669,0,64218,85795,2449,48939,12869],
            [93539,28909,90973,77642,0,72170,98359],
            [88628,16422,80512,0,38651,50854,55768],
            [13639,2889,74835,80416,26051,78859,25721],
            [90182,23154,16586,0,27459,3272,84893],
            [2480,33654,87321,93272,93079,0,38394],
            [34676,72427,95024,12240,72012,0,57763],
            [97957,56,83817,45472,0,24087,90245],
            [32056,0,92049,21380,4980,38458,3490],
            [21509,76628,0,90430,10113,76264,45840],
            [97192,58807,74165,65921,45726,47265,56084],
            [16276,27751,37985,47944,54895,80706,2372],
            [28438,53073,0,67255,38416,63354,69262],
            [23926,75497,91347,58436,73946,39565,10841],
            [34372,69647,44093,62680,32424,69858,68719],
            [24425,4014,94871,1031,99852,88692,31503],
            [24475,12295,33326,37771,37883,74568,25163],
            [0,18411,88185,60924,29028,69789,0],
            [34697,75631,7636,16190,60178,39082,7052],
            [24876,9570,53630,98605,22331,79320,88317],
            [27204,89103,15221,91346,35428,94251,62745],
            [26636,28759,12998,58412,38113,14678,0],
            [80871,79706,45325,3861,12504,0,4872],
            [79662,15626,995,80546,64775,0,68820],
            [25160,82123,81706,21494,92958,33594,5243]
        ],
        5637),
    ]

    for item in data:
        m, answer = item
        result = Solution().cutOffTree(m)
        print(result == answer, result, answer)
