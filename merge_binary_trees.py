# Merge Two Binary Trees

#  Tree 1           Tree 2        ->  Merged tree
#           1               2            	     3
#          / \             / \                  / \
#         3   2           1   3                4   5
#        /                \   \               / \   \
#       5                 4   7              5   4   7

class Solution(object):
    def mergeTrees(self, t1, t2):

        if t1 is None and t2 is None:
            return None
        if t1 is None or t2 is None:
            return t1 if t1 else t2

        t3 = TreeNode(0)
        queue = [ (t1, t2, t3) ] # [left, right, root]
        while(len(queue)):

            lt, rt, root = queue.pop(0)
            root.val = lt.val + rt.val

            if lt.left and rt.left:
                root.left = TreeNode(0)
                queue.append(( lt.left, rt.left, root.left ) )

            elif lt.left or rt.left:
                root.left = lt.left if lt.left else rt.left

            if lt.right and rt.right:
                root.right = TreeNode(0)
                queue.append(( lt.right, rt.right, root.right ))
            elif lt.right or rt.right:
                root.right = lt.right if lt.right else rt.right

        return t3


if __name__ == '__main__':
# ================================================
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
# ================================================

    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(4)

    t2 = TreeNode(2)
    t2.left = TreeNode(5)
    t2.right = TreeNode(6)

    t2.right.left = TreeNode(2)

    t3 = Solution().mergeTrees(t1, t2)

    print(t3.val)
    print(t3.left.val)
    print(t3.right.val)
