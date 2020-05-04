# Binary Tree Maximum Path Sum

# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Given a non-empty binary tree, find the maximum path sum.
# For this problem, a path is defined as any sequence of nodes from some starting
# node to any node in the tree along the parent-child connections.
# The path must contain at least one node and does not need to go through the root.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    MAX_PATH = float("-inf") # -infinity

    def maxPathSum(self, root):

        items = [root.val]

        if root.left is not None:
            self.maxPathSum(root.left)
            items.append(root.val + root.left.val)
        if root.right is not None:
            self.maxPathSum(root.right)
            items.append(root.val + root.right.val)

        max_path = max(items)

        if root.left is not None and root.right is not None:
            items.append(root.val + root.right.val + root.left.val)

        self.MAX_PATH = max(max(items), self.MAX_PATH)
        root.val = max_path

        return self.MAX_PATH


def build_tree(list):
        idx = 0
        root = TreeNode(list[idx])
        queue = [root]

        while(len(queue)):
            node = queue.pop(0)
            idx += 1
            if idx < len(list) and list[idx] is not None:
                node.left = TreeNode(list[idx])
                queue.append(node.left)
            idx += 1
            if idx < len(list) and list[idx] is not None:
                node.right = TreeNode(list[idx])
                queue.append(node.right)

        return root


if __name__ == '__main__':

    data = [
        ([5,4,8,11,None,13,4,7,2,None,None,None,1], 48),
        ([1,-2,-3,1,3,-2,None,-1],                  3),
        ([-10,9,20,None,None,15,7],                 42),
        ([-1, 2, 2],                                3),
        ([1,2,3, -1, 5, -1, 6],                     17),
    ]

    for item in data:
        l, answer = item
        root = build_tree(l)
        result = Solution().maxPathSum(root)
        print(result == answer, answer)
