def find_max_consecuitive_sum(list):
    print list

    max = list[0]
    sum = list[0]

    for item in (list[1:]):
        sum = sum + item
        if sum > max:
            max = sum
        elif item > sum:
            sum = item
            max = sum if sum > max else max
    return max

# example:
# list = [6] # -> [6, 0, 0]
# list = [6, -1] # -> [6, 0, 0]
# list = [6, -1, 2] # -> 7, 0, 2
# list = [6, -1, 2, -10] # -> 7, 0, 2
# list = [6, -1, 2, -10, 8] # -> 8, 4, 4

list = [0,-1, 2, 3, -8]
print find_max_consecuitive_sum(list)

'''
list = [-1, 2, -3, 2, 4, -3, 2, 5 , -1]
print find_max_consecuitive_sum(list)

list = [6, -1, 2, -10, 8]
print find_max_consecuitive_sum(list)

list = [6, -1, 5, -17, 3]
print find_max_consecuitive_sum(list)

list = [6, -1, 5, -17, 3, 9]
print find_max_consecuitive_sum(list)
'''
