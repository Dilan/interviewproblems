def find_sub_array(list):
    if len(list) == 1:
        return list
    sub = find_sub_array(list[1:])
    l = [(list[0] + x) for x in sub]

    return [list[0]] + sub + l

def is_sum_exist(n, list):
    return n in find_sub_array(list)

print is_sum_exist(2, [3,2,1])
print is_sum_exist(5, [3,2,1])
print is_sum_exist(6, [3,2,1])
print is_sum_exist(7, [3,2,1])