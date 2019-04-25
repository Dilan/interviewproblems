class Solution(object):

    def couldItBeBatter(self, idx, current_max, s):
        l = len(s[0:idx])
        r = len(s[idx:])

        return (min(l, r) * 2 ) + 1 > current_max

    def findPalindrome(self, palindrom, s):
        left = palindrom[0] - 1
        right = palindrom[-1] + 1

        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break

            palindrom = [left] + palindrom + [right]
            left -= 1
            right += 1

        return palindrom

    def longestPalindrome(self, s):

        if len(s) == 0:
            return s

        # special structure
        # ======================================================================
        #     1   3   5   7   9   11
        #  [A] [B] [C] [B] [A] [W] [X]
        #   0   2   4   6   8  10  12
        # ======================================================================
        #  _odd_ is a number,
        #  _even_ is space between numbers


        max_substr = []
        exS = (len(s) - 1) * 2
        median = exS / 2

        queue = [median]
        while len(queue):
            j = queue.pop(0)

            m = None
            if j % 2 == 0:
                i = j / 2
                m = [i]
            else:
                i = (j-1) / 2
                k = (j+1) / 2

                if i >= 0 and k < len(s) and s[i] == s[k]:
                    m = [i, k]

            if m is not None:
                palindrom = self.findPalindrome(m, s)
                if len(palindrom) > len(max_substr):
                    max_substr = palindrom


                if self.couldItBeBatter(i, len(max_substr), s) is False:
                    break


            # next_i = (i-1) if i <= median else (i + 1)

            if j >= median and (j+1) < exS:
                queue.append(j+1)
            if j <= median and (j-1) >=0:
                queue.append(j-1)

        s0 = max_substr[0]
        sL = max_substr[-1]+1

        return s[s0:sL]



if __name__ == '__main__':
    s = "eabcb"
    result = Solution().longestPalindrome(s)
    print(s + ' ==>', result, len(result), 'vs', len(s))

    s = 'ababc'
    result = Solution().longestPalindrome(s)
    print(s + ' ==>', result, len(result), 'vs', len(s))

    s = 'cbbd'
    result = Solution().longestPalindrome(s)
    print(s + ' ==>', result, len(result), 'vs', len(s))

    s = 'aaaaaaaacbaaaaaa'
    result = Solution().longestPalindrome(s)
    print(s + ' ==>', result, len(result), 'vs', len(s))
    #
    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # result = Solution().longestPalindrome(s)
    # print(s + ' ==>', result, len(result), 'vs', len(s))

    s = "dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"
    result = Solution().longestPalindrome(s)
    print(s + ' ==>', result, len(result), 'vs', len(s))



    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # result = Solution().longestPalindrome(s)
    # print(s + ' ==>', result, len(result), 'vs', len(s))
