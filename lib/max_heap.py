def max_heapify(list, i):
    left = (i*2) + 1
    right = (i*2) + 2
    largest = i

    if left < len(list) and list[left] > list[largest]:
        largest = left
    if right < len(list) and list[right] > list[largest]:
        largest = right

    if largest != i:
        list[largest], list[i] = list[i], list[largest]
        max_heapify(list, largest)
    return list

def build_max_heap(list):
    for i in range(len(list) / 2 - 1, -1, -1):
        max_heapify(list, i)
    return list

#        6         ||             12
#   12       1     ||   =>     7       8
# 3    7   8   4   ||        3   6   1   4


print build_max_heap([6, 12, 1, 3, 7, 8, 4])