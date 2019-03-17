def sieve_of_eratosthenes(limit):
    arr = [False, False] + [True] * (limit-2)

    for i, is_prime in enumerate(arr):
        if is_prime:
            # yield i
            for k in xrange(i*i, limit, i):
                arr[k] = False
    return arr


def primes(limit):
    arr = sieve_of_eratosthenes(limit)
    plist = []
    for idx, val in enumerate(arr):
        if val:
            plist.append(idx)
    return plist

print(primes(25))
# print(sieve_of_eratosthenes(20))
