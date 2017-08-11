# -*- coding: utf-8 -*-

# https://cmind.kattis.com/problems/coast

# You will be given a map of Soteholm as an N×M grid.

#         N
#  ~   ~  ~   ~
#  ~   __ __  ~
#  ~  |__|__| ~    M
#  ~  |__| ~  __
#  ~   ~   ~ |__|
#  ~   ~  ~   ~

# Each square in the grid has a side length of 1 km and is either water or land.
# Your goal is to compute the total length of sea coast of all islands.
# Sea coast is all borders between land and sea, and sea is any water connected
# to an edge of the map only through water.

# Two squares are connected if they share an edge. You may assume that the map is
# surrounded by sea. Lakes and islands in lakes are not contributing to the sea coast.

def neigbours(x,y,coast):
    result = []
    conditions = [
        lambda x,y: (x+1,y),
        lambda x,y: (x-1,y),
        lambda x,y: (x,y+1),
        lambda x,y: (x,y-1)
    ]
    for xy in conditions:
        x0, y0 = xy(x,y)
        if x0 >= 0 and x0 < len(coast) and y0 >=0 and y0 < len(coast[x0]):
            result.append((x0,y0))
    return result

def swim(x,y,coast,visited):
    visited[(x,y)] = True
    for xy in neigbours(x,y,coast):
        if coast[xy[0]][xy[1]] == "0" and (xy[0],xy[1]) not in visited:
            swim(xy[0], xy[1], coast, visited)

def calculate_coast_length(input):
    # wrap with more sea water
    coast = []
    coast.append(['0'] * (2+len(input[0])))
    for row in input:
        coast.append(['0'] + list(row) + ['0'])
    coast.append(['0'] * (2+len(input[0])))

    visited = { }
    swim(0, 0, coast, visited)

    # mark lakes
    for x, line in enumerate(coast):
        for y, val in enumerate(line):
            if val == '0' and (x,y) not in visited:
                coast[x][y] = 'w'

    counter = 0
    for x, line in enumerate(coast):
        for y, val in enumerate(line):
            if val == '1':
                for xy in neigbours(x,y,coast):
                    if coast[xy[0]][xy[1]] == '0':
                        counter +=1

    return counter

if __name__ == '__main__':
    print(
        calculate_coast_length([
            "00011",
            "01101",
            "01001",
            "00110"
        ])
    )
