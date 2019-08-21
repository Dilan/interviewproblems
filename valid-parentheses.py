class Solution(object):
    def isValid(self, s):
        value = {
            "{":1,"}":1,
            "[":2,"]":2,
            "(":3,")":3,
        }

        stack = []
        for k in s:
            if k in ["}", "]", ")"]:
                if len(stack) == 0 or value[k] != value[stack.pop()]:
                    return False
            else:
                stack.append(k)

        return len(stack) == 0

if __name__ == "__main__":

    data = [
        ('()[]{}', True),
        ('([)]', False),
        ('(', False),
    ]

    for item in data:
        str, answer = item
        result = Solution().isValid(str)
        print(result == answer)
