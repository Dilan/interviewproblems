import collections

# x = collections.Counter({'red': 4, 'blue': 2})
# x['blue'] = 0
# print x

def minWindow(s, t):
    need, missing = collections.Counter(t), len(t)

    i = I = J = 0
    for j, c in enumerate(s, 1):
        missing -= need[c] > 0
        need[c] -= 1

        if not missing:
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
                
            if not J or j - i <= J - I:
                I, J = i, j
    return s[I:J]

print minWindow("AXXBCXXXXBA", "ABC")
print minWindow("WADWBECODEBA", "ABC")
print minWindow("WADOBECODEBANC", "ABC")
