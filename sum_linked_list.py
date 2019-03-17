# https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def toNum(self,l):
        num = []
        while True:
            num.append(str(l.val))
            if l.next is None:
                break
            l = l.next
        num.reverse()
        return int(''.join(num))

    def toListNode(self, num):
        num = str(num)
        root, node = None, None

        for i in list(num)[::-1]:
            if root is None:
                root = ListNode(int(i))
                node = root
                continue

            node.next = ListNode(int(i))
            node = node.next

        return root

    def addTwoNumbers(self, l1, l2):
        num1 = self.toNum(l1)
        num2 = self.toNum(l2)

        return self.toListNode(num1 + num2)

# CLI
if __name__ == '__main__':
    # 8 -> 9 -> 9
    l1 = ListNode(8)
    l11 = ListNode(9)
    l111 = ListNode(9)
    l11.next = l111
    l1.next = l11
    # 2
    l2 = ListNode(2)

    result = Solution().addTwoNumbers(l1, l2)
    print(result.val)
    print(result.next.val)
    print(result.next.next.val)
    print(result.next.next.next.val)
