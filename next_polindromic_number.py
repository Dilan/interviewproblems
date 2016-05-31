def is_polindromic(value):
    for idx in range(len(value)/2):
        if value[idx] != value[-(idx+1)]:
            return False
    return True

def next_polindromic_number(num):
    next = num + 1
    while True:
        if is_polindromic(str(next)):
            return next
        next += 1

print next_polindromic_number(99) # 101
print next_polindromic_number(6789876) # 6790976
