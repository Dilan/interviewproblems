# https://leetcode.com/problems/distance-between-bus-stops/

# A bus has n stops numbered from 0 to n - 1 that form a circle.
# We know the distance between all pairs of neighboring stops where distance[i]
# is the distance between the stops number i and (i + 1) % n.

# The bus goes along both directions i.e. clockwise and counterclockwise.

# Return the shortest distance between the given start and destination stops.

class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):

        N = len(distance)
        result1, result2 = 0, 0

        i = start
        while i != destination:
            result1 += distance[i]
            i = (i + 1) % N

        i = destination
        while i != start:
            result2 += distance[i]
            i = (i + 1) % N

        return min(result1, result2)

if __name__ == '__main__':
    data = [
        ([7,10,1,12,11,14,5,0], 7, 2, 17),
        ([1,2,3,4], 0, 3, 4)
    ]

    for item in data:

        distance, start, destination, answer = item
        result = Solution().distanceBetweenBusStops(distance, start, destination)

        print(result, answer)
