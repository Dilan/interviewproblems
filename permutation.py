def insertTo(index, val, list):
    return list[:index] + [val] + list[index:]

def permutation(list):
    if len(list) == 1:
        return [list]

    ps = permutation(list[1:])

    print ps

    l = []
    for p in ps:
        for i in range(len(p)+1):
            l.append(insertTo(i, list[0], p))

    return l

print permutation([1,2,3,4])
