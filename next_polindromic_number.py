def is_polindromic(value):
    for idx in range(len(value)/2):
        if value[idx] != value[-(idx+1)]:
            return False
    return True

def next_polindromic_number_incremental(num):
    next = num + 1
    while True:
        if is_polindromic(str(next)):
            return next
        next += 1

# ================================================

# solution: O(1)
def split_num(number):
    length = len(number)
    left = number[:length/2]
    middle = int(number[length/2]) if length % 2 else None
    right = number[length/2+1:] if length % 2 else number[length/2:]

    return (int(left), middle, int(right))

def reverse(num):
    return str(num)[::-1]

def next_polindromic_number(num):
    l, m, r = split_num(str(num+1))

    if m is None:
        if int(reverse(l)) >= r:
            return int(str(l) + reverse(l))
        else:
            return int(str(l+1) + reverse(l+1))
    else:
        if int(reverse(l)) >= r:
            return int(str(l) + str(m) + reverse(l))
        else:
            if m < 9:
                return int(str(l) + str(m+1) + reverse(l))
            else:
                return int(str(l+1) + str(0) + reverse(l+1))

def check_polindromic(num):
    flag = next_polindromic_number(num) == next_polindromic_number_incremental(num)
    print str(num) + ' -> ' + str(next_polindromic_number(num)) + ' (' + str(flag) + ')'

check_polindromic(99)
check_polindromic(12024)
check_polindromic(1224)
check_polindromic(1219)
check_polindromic(12932)
check_polindromic(12419)
check_polindromic(12432)
check_polindromic(12919)
