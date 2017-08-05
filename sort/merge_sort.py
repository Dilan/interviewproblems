def merge_sort(l):
    if len(l)<2:
        return l,0

    x1,x2 = divide(l)
    x1,li = merge_sort(x1)
    x2,ri = merge_sort(x2)
    merged,si = merge(x1,x2)
    return merged,(li+si+ri)

def divide(list):
    half = len(list)/2
    return list[0:half], list[half:]

def merge(x1,x2):
    x = []
    idx1 = 0
    idx2 = 0
    inv_count = 0

    size1=len(x1)
    size2=len(x2)

    while (idx1 < size1) and (idx2 < size2):
        if x1[idx1]<=x2[idx2]:
            x.append(x1[idx1])
            idx1 += 1
        else:
            x.append(x2[idx2])
            idx2 += 1
            inv_count += (size1-idx1)

    for i in range(idx1,size1):
        x.append(x1[i])

    for i in range(idx2,size2):
        x.append(x2[i])

    return x,inv_count
