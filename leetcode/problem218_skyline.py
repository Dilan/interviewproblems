# The SKYLINE problem
# You are given a set of n rectangles in no particular order.
# They have varying widths and heights, but their bottom edges are collinear,
# so that they look like buildings on a skyline.
# For each rectangle, you are given the x position of the left edge, the x position of the
# right edge, and the height.
# Your task is to draw an outline around the set of rectangles so that you can see
# what the skyline would look like when silhouetted at night.

# 8      _____                     _____
# 7     |     |                   |     |
# 6   __|_    |  result is:     __|     |
# 5  |  | |   |                |        |
# 4  |  | |   |                |        |
# 3  |  | |   |                |        |
# 2  |  | |   |                |        |
# 1  |  | |   |                |        |
# --------------------------------------------->
#    1  3 5   7                1  3     7
#
# [x1, height, x2]
# input = [ [1,6,5], [3,8,7] ]
# output has to be [[1,6], [3,8], [7,0]

def skyline(input):
    if len(input) == 0:
        return []

    # fix [x1, x2, height] --> [x1, height, x2]
    for line in input: 
        line[1],line[2] = line[2],line[1]

    hm = {}
    for item in input:
        for x in range(item[0], item[2]):
            if x in hm:
                hm[x] = hm[x] if hm[x] > item[1] else item[1]
            else:
                hm[x] = item[1]

        if item[2] not in hm:
            hm[item[2]] = 0

    print('...',hm)

    output = []
    for x in range(min(hm.keys()), max(hm.keys())+1):
        if x not in hm:
            hm[x] = 0

        if len(output) == 0:
            output.append([x, hm[x]])
            continue

        last = output[len(output)-1]
        if last[1] != hm[x]:
            output.append([x, hm[x]])

    return output


print skyline([ [0,7,10] ])

# print skypine([[ 2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
# [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]

# print skypine([ [1,11,5], [2,6,7], [3,13,9], [12,7,16]])
# print skypine([ [1,11,5], [2,6,7], [3,13,9], [12,7,16], [14,3,25], [19,18,22], [23,13,29], [24,4,28] ])
