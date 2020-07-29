class Solution(object):
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [[num] + arr for arr in result]
        return result

    def subsets_dfs(self, nums):
        res = []
        self.dfs([], res, 0, nums)
        return res

    def dfs(self, path, res, n, nums):
        res.append(path)
        for i in range(n, len(nums)):
            self.dfs(path + [nums[i]], res, i+1, nums)



if  __name__ == '__main__':
    data = [
        (
            [1,2,3],
            [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]
        ),

    ]

    for item in data:
        nums, answer = item
        result = Solution().subsets_dfs(nums)
        print(nums)
        print('Result (recursively)')
        print(result)

        print('Result (Iteratively)')
        result = Solution().subsets(nums)
        print(result)
