def get_product(num, list, exception_index):
    result = num
    for idx, n in enumerate(list):
        if idx != exception_index:
            result *= n
    return result

def cut_the_rope(length):
    collection = [
        { 'max': 0, 'variants': [0] },
        { 'max': 1, 'variants': [1] },
        { 'max': 2, 'variants': [1,1] },
        { 'max': 3, 'variants': [1,2] }
    ]

    if length < 3:
        return collection[length]['variants']

    for n in range(4, length+1):
        max = 0
        prev_variants = collection[n-1]['variants']
        variants = []

        for idx, v in enumerate(prev_variants):
            prod = get_product(collection[v + 1]['max'], prev_variants, idx)

            if v+1 == 2 or v+1 == 3:
                cvar = [v+1]
            else:
                cvar = collection[v + 1]['variants']

            if max < prod:
                max = prod
                variants = prev_variants[:idx] + cvar + prev_variants[idx+1:]

        collection.append({ 'idx': n, 'max': max, 'variants': variants })

    print collection

cut_the_rope(12)

