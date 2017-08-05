def reverse_string(value):
    if (value == ''):
        return ''
    return reverse_string(value[1:]) + value[0]

print reverse_string('abc')