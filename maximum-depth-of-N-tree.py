# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

# Given a n-ary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    @staticmethod
    def dfs_recursion(root, depth=1):
        max_depth = depth
        if root.children is not None and len(root.children) > 0:
            for n in root.children:
                val = Solution.dfs(n, depth + 1)
                max_depth = max(val,max_depth)

        return max_depth

    @staticmethod
    def dfs(root):
        max_depth = 0
        stack = [(root, 1)]
        while len(stack):
            node, depth = stack.pop(0)
            max_depth = max(depth,max_depth)
            if node.children is not None and len(node.children) > 0:
                for n in node.children:
                    stack.extend([(n, depth + 1)])
        return max_depth

    @staticmethod
    def bfs(root):
        max_depth = 0
        stack = [(root, 1)]
        while len(stack):
            node, depth = stack.pop(0)
            max_depth = max(depth,max_depth)
            if node.children is not None and len(node.children) > 0:
                for n in node.children:
                    stack.extend([(n, depth + 1)])
        return max_depth

    def maxDepth(self, root):
        if root is None: return 0

        max_depth = Solution.dfs(root)
        return max_depth


if __name__ == '__main__':
    root = Node(1, [Node(2),Node(3), Node(4)])

    answer = Solution().maxDepth(root)
    print(answer)
