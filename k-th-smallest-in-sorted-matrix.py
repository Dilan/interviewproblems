# Given a n x n matrix where each of the rows and columns are sorted in ascending order,
# find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

from heapq import heappush, heappop

class Solution(object):
    def kthSmallest(self, matrix, k):

        heap = []
        pointer = len(matrix) * [0]
        x_size = len(matrix[0])
        result = []

        for idx, line in enumerate(matrix):
            heappush(heap, (line[0], (0, idx))) # (weight, x/y)
            pointer[idx] = 1

        while k > 0:

            k -= 1
            item, point = heappop(heap)
            x, y = point
            result.append(item)

            if k == 0:
                break

            if (x+1) < len(matrix[0]):
                heappush(heap, (matrix[y][x+1], (x+1,y))) # (weight, x/y)
                pointer[y] = x+1
            else:
                for j,i in enumerate(pointer):
                    if x_size < (i+1):
                        pointer[j] = i+1
                        ii = pointer[j]
                        heappush(heap, (matrix[j][ii], (ii,j)))

        return result[-1]

if __name__ == '__main__':
    data = [
        ([
           [ 1,5,9],[10,11,13],[12,13,15]
        ], 8, 13),
        ([
           [1,3,5],[6,7,12],[11,14,14]
        ], 8, 14),
        ([
           [-5]
        ], 1, -5),

    ]

    for item in data:
        m, k, answer = item
        result = Solution().kthSmallest(m, k)
        print(result == answer)
