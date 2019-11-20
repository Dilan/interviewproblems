# Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.
#
# Example 1:
# Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]
#
#        5
#       / \
#     3    6
#    / \    \
#   2   4    8
#  /        / \
# 1        7   9
#
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
#  1
#   \
#    2
#     \
#      3
#       \
#        4
#         \
#          5
#           \
#            6
#             \
#              7
#               \
#                8
#                 \
#                  9

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

class Solution(object):

    @staticmethod
    def dfs(node, result):
        if node.left is not None:
            Solution.dfs(node.left, result)

        result.append(node.val)

        if node.right is not None:
            Solution.dfs(node.right, result)

        return result

    def increasingBST(self, root):

        result = []
        self.dfs(root, result)
        rNode = TreeNode(result.pop(0))

        node = rNode
        while len(result):
            item = result.pop(0)
            node.right = TreeNode(item)
            node = node.right
        return rNode


if __name__ == '__main__':
    root = build_tree(
        [5,3,6,2,4,None,8,1,None,None,None,7,9]
    )
    node = Solution().increasingBST(root)

    # print answer:
    space = 0
    while node is not None:
        space += 1
        print(("-".join([' '] * space)) + str(node.val))
        node = node.right
