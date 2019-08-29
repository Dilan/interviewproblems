"""
https://leetcode.com/problems/path-sum-ii/
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Given the below binary tree and sum = 22,

          [5]
          / \
        [4]   [8]
       /      / \
      [11]   13  [4]
     /  \        / \
    7    [2]    [5]   1

Answer:
[[5,4,11,2], [5,8,4,5]]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        if (root is None):
            return []

        result = []
        queue = [(root, (sum - root.val), [root.val])]

        while(len(queue)):
            node, rest, list = queue.pop()

            if rest == 0 and (node.left is None and node.right is None):
                result.append(list)

            else:
                items = []
                if node.left is not None:
                    items.append(node.left)
                if node.right is not None:
                    items.append(node.right)

                for n in items:
                    queue.append((n, rest-n.val, list + [n.val]))

        return result

    @staticmethod
    def build_tree(list):

        idx = 0
        root = TreeNode(list[idx])
        queue = [root]

        while(len(queue)):
            node = queue.pop(0)

            for n in [node.left, node.right]:
                idx += 1
                if idx < len(list) and list[idx] is not None:
                    n = TreeNode(list[idx])
                    queue.append(n)

        return root

if __name__ == "__main__":

    data = [
        (
            [5,4,8,11,None,13,4,7,2,None,None,5,1], 22,
            [[5,4,11,2],[5,8,4,5]]
        ),
        (
            [1,2], 1,
            [[1]]
        ),
        (
            [-2,None,-3],-5,
            [[-2,-3]]
        ),

    ]

    for item in data:
        list, s, answer = item
        root = Solution.build_tree(list)
        result = Solution().pathSum(root, s)

        print(result, answer)
