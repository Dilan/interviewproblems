# Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it.
# Find and return the shortest palindrome you can find by performing this transformation.

 # "aacecaaa" --> "aaacecaaa"
 # "abcd"     --> "dcbabcd"

class Solution(object):
    @staticmethod
    def isPalindrome(left, right):
        return left[::-1] == right[0:len(left)]

    @staticmethod
    def cut(idx, s):
        i = idx / 2

        if (idx % 2) == 0:
            return (s[0:i],s[i+1:], s[i])
        return (s[0:i+1],s[i+1:], '')

    def shortestPalindrome(self, s):
        midx = len(s) - 1

        if midx <= 0:
            return s

        while midx >= 0:
            left, right, middle = Solution.cut(midx, s)
            if Solution.isPalindrome(left, right):
                break
            midx -= 1

        reflected = right[len(left):][::-1]
        return (reflected + left + middle + right)

s = Solution()

print(s.shortestPalindrome("5414567"))
print(s.shortestPalindrome("544567"))
print(s.shortestPalindrome("76567"))
print(s.shortestPalindrome("12345"))
print(s.shortestPalindrome("7655679"))
print(s.shortestPalindrome("aacecaaa"))
print(s.shortestPalindrome("76515678"))
