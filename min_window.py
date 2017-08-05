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
        
        # print c, ') missing=',missing
        
        if not missing:
            # print c,') s[', i, ']', s[i], 'need', need, need[s[i]]
            print c,j,') s[', i, ']=', s[i], need
            
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
                print 'so...', need, 'i = ', i, 'j - i', j - i, 'vs', J-I
            if not J or j - i <= J - I:
                I, J = i, j
                print 'hm... [', I, J, ']'
    return s[I:J]

print minWindow("AXXBCXXXXBA", "ABC")
# print minWindow("WADWBECODEBA", "ABC")
# print minWindow("WADOBECODEBANC", "ABC")
