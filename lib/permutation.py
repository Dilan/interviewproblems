def permutation(list):
    if len(list) == 1:
        return [list]
    l = []
    for p in permutation(list[1:]):
        for i in range(len(p)+1):
            l.append(p[:i] + [list[0]] + p[i:])
    return l

def permutation_inplace(a, k=0, result=[]):
    print a
    if k == len(a):
        return result.append(a[:])

    for i in range(k,len(a)):
        a[k],a[i] = a[i], a[k]
        permutation_inplace(a, k+1, result)
        a[i],a[k] = a[k], a[i]

    return result
