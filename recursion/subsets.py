# all available subsets
def subset(list):
    if len(list) == 1:
        return [list]

    result = [[list[0]]]
    for s in subset(list[1:]):
        result.append(s)
        result.append([list[0]] + s)

    return result
