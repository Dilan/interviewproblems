class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root, target):


        def dfs(node, target):

            if node.left is None and node.right is None:
                return node

            x = None
            if target > node.val :
                if node.right is None:
                    return node

                x = dfs(node.right, target)

            else:
                if node.left is None:
                    return node

                x = dfs(node.left, target)


            if abs(target - x.val) < abs(target - node.val):
                return x

            return node


        return dfs(root, target).val



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
        ([4,2,7,1,3,6,9], 10, 9),
        ([4,2,7,1,3,6,9],  5, 4),
        ([4,2,7,1,3,5,10], 11, 10),
        ([4,2,7,1,3,5,10], 1.6, 2),
    ]

    for item in data:
        l, target, answer = item
        root = build_tree(l)

        result = Solution().find(root, target)
        print(result.val == answer, result.val, 'vs', answer)
