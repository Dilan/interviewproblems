"""
https://leetcode.com/problems/game-of-life/

Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the
following four rules (taken from the above Wikipedia article):

- Any live cell with fewer than two live neighbors dies, as if caused by under-population.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by over-population..
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.
The next state is created by applying the above rules simultaneously to every cell in the current
state, where births and deaths occur simultaneously.

0 1 0       0 0 0
0 0 1       1 0 1
1 1 1  ->   0 1 1
0 0 0       0 1 0
"""

class Solution(object):
    def neighbors_weight(self, point, board):
        x, y = point

        weight = 0
        lx = max(x-1, 0)
        rx = min(x+1, len(board[0])-1)
        ly = max(y-1, 0)
        ry = min(y+1, len(board)-1)

        for y0 in range(ly, ry + 1):
            for x0 in range(lx, rx + 1):
                if x0 != x or y0 != y:
                    weight += board[y0][x0]

        return weight

    def gameOfLife(self, board):
        clone_board = [line[:] for line in board]

        for y, line in enumerate(board):
            for x, v in enumerate(line):
                weight = self.neighbors_weight((x,y),clone_board)

                if (v == 0 and weight == 3) or (v == 1 and weight in [2,3]):
                    board[y][x] = 1
                else:
                    board[y][x] = 0


def print_matrix(*args):
    boards = list(args)
    for idx, line in enumerate(boards[0]):
        s = " ".join(str(x) for x in line) + "\t"
        for b in boards[1:]:
            s += " ".join(str(x) for x in b[idx]) + "\t"
        print s

if __name__ == '__main__':
    data = [
        ([
            [0,1,0],
            [0,0,1],
            [1,1,1],
            [0,0,0]
        ], [
            [0,0,0],
            [1,0,1],
            [0,1,1],
            [0,1,0]
        ])
    ]

    for item in data:
        board, answer = item
        original_board = [line[:] for line in board]
        Solution().gameOfLife(board)
        print_matrix(original_board, board, answer)
