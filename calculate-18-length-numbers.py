
# How many 18-digit number is there such that no digit occurs more than 3 times. 
# All numbers start with a non-zero digit.

def insertTo(index, val, list):
    return list[:index] + [val] + list[index:]

def permutation(list):
    if len(list) == 1:
        return [list]

    ps = permutation(list[1:])

    # print ps

    l = []
    for p in ps:
        for i in range(len(p)+1):
            l.append(insertTo(i, list[0], p))

    return l

print len(permutation([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]))
