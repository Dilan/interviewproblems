def quick_sort_recursion(list):
    if len(list) < 2:
        return list

    left = []
    right = []
    pivot = list.pop()

    for item in list:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)

    return quick_sort_recursion(left) + [pivot] + quick_sort_recursion(right)

# in place with O(1) memory
def partition(list, begin, end):
    pivot = begin

    for i in range(begin+1, end+1):
        if list[begin] > list[i]:
            pivot += 1
            list[i], list[pivot] = list[pivot], list[i]
    # move 1st element to [pivot] position
    list[pivot], list[begin] = list[begin], list[pivot]
    return pivot

def quick_sort(list, begin=None, end=None):
    # default
    begin = 0 if begin is None else begin
    end = len(list)-1 if end is None else end

    if begin > end:
        return

    pivot = partition(list, begin, end)
    quick_sort(list, begin, pivot-1)
    quick_sort(list, pivot+1, end)

list = [4,1,2,3,8,9,6]
# list = [3,5,4,1,2]
quick_sort(list)
print list
