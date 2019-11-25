class Solution(object):
    def isSubsequence(self, s, t):

        j, amount = 0, 0
        size = len(t)

        for i in range(len(s)):
            while j < size:
                flag = (t[j] == s[i])
                j += 1

                if flag:
                    amount += 1
                    break

            if amount < (i + 1):
                break

        return len(s) == amount

if __name__ == '__main__':
    data = [
        ("abc", "ahbgdc", True),
    ]

    for item in data:

        s, t, answer = item
        result = Solution().isSubsequence(s, t)

        print(result, answer)
