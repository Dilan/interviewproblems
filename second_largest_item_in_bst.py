# https://www.interviewcake.com/question/python/second-largest-item-in-bst

# Write a function to find the 2nd largest element in a binary search tree.

def second_largest(node):
    list = dfs_largest(node)
    last = list[len(list) - 1]
    penult = list[len(list) - 2]
    return penult if last > penult else last

def dfs_largest(node):
    list = [node['value']]
    if node['right'] or node['left']:
        list.extend(dfs_largest(node['right'] if node['right'] else node['left']))
    return list

def create_tree(list):
    hm = {}
    for data in list:
        value = data[0]
        left = data[1] if len(data) > 1 else None
        right = data[2] if len(data) > 2 else None

        if value not in hm:
            hm[value] = { 'value': value }
        if left is not None and left not in hm:
            hm[left] = { 'value': left, 'right': None, 'left': None }
        if right is not None and right not in hm:
            hm[right] = { 'value': right, 'right': None, 'left': None }

        hm[value]['left'] = hm[left]
        hm[value]['right'] = hm[right] if right in hm else None

    return hm

# test [1]
bst = create_tree([[50,30,80], [30,20,40], [80,60,90]])
assert 80 == second_largest(bst[50])

# test [2]
bst = create_tree([[50,30,80], [30,20,40], [80,60]])
assert 60 == second_largest(bst[50])
