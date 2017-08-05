
# non recursive
def wildcard(input):
    variants = []
    for letter in list(input):
        if letter == '?':
            clone = []
            for v in variants:
                clone.append(v + ['0'])
                v.append('1')
            variants.extend(clone)
        else:
            if len(variants) == 0:
                variants.append([letter])
            else:
                for v in variants:
                    v.append(letter)

    return [''.join(items) for items in variants]

# print ', '.join(wildcard('10?'))
# print ', '.join(wildcard('1?01'))
# print wildcard('1?01')
# print ', '.join(wildcard('1?0?'))

def _wildcard(list):
    additional = []
    for r in list:
        numbers = ['0','1']
        for idx, num in enumerate(numbers):
            if idx == len(numbers)-1:
                r.append(num)
            else:
                additional.append(r + [num])
    list.extend(additional)
    return list

def _wildcard_(input, n, result):
    if n > len(input)-1:
        return result

    letter = input[n]
    if letter == '?':
        _wildcard(result)
    else:
        for v in result:
            v.append(letter)

    return _wildcard_(input, n+1, result)

str = '10?'
print ', '.join([''.join(items) for items in _wildcard_(list(str), 0, [[]])])
str = '1?0?'
print ', '.join([''.join(items) for items in _wildcard_(list(str), 0, [[]])])

