# -*- coding: utf-8 -*-

# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

class Solution(object):
    def decodeString(self, s):
        s = unicode(s, 'utf')
        str = ""
        queue = []
        for idx, k in enumerate(s):

            if k.isnumeric():
                if idx > 0 and s[idx-1].isnumeric():
                    queue[-1][0] += k
                else:
                    queue.append([k, ""])
            elif k == "[":
                pass
            else:
                if k == "]":
                    item = queue.pop()
                    k = int(item[0]) * item[1]

                if len(queue) > 0:
                    queue[-1][1] += k
                else:
                    str += k

        return str.encode('ascii','ignore')

if __name__ == "__main__":

    data = [
        ('3[a]2[bc]', 'aaabcbc'),
        ('3[a2[c]]', 'accaccacc'),
        ('2[abc]3[cd]ef', 'abcabccdcdcdef'),
        ('10[c]', 'cccccccccc'),
    ]

    for item in data:
        str, answer = item
        result = Solution().decodeString(str)
        print(result, answer, result == answer)
