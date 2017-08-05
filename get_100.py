# Write a program that outputs all possibilities to put + or - or nothing between the numbers 1, 2, ..., 9
# (in this order) such that the result is always 100.
#
# For example: 1 + 2 + 34 - 5 + 67 - 8 + 9 = 100

def join(num1, num2):
    return int(str(num1) + str(num2))

def f(numbers, item=None):
    if item is None:
        return f(numbers[1:], numbers[0])
    if len(numbers) == 0:
        return [item]

    result = []

    # 1st (concat)
    result.extend(f(numbers[1:], join(item, numbers[0])))
    # 2nd (+)
    for p in f(numbers[1:], numbers[0]):
        result.extend([item + p])
    # 3rd (-)
    for p in f(numbers[1:], -1*numbers[0]):
        result.extend([item + p])

    return result

counter = 0
result = f(range(1,10))

for i in result:
    if i == 100:
        counter += 1

print counter