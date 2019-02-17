class Solution(object):
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            for arr in result[:]:
                result.append([num]+arr)
        return result

    def subset_recursion(self, list):
        if len(list) == 1:
            return [list]

        result = [[list[0]]]
        for s in self.subset_recursion(list[1:]):
            result.append(s)
            result.append([list[0]] + s)

        return result

if  __name__ == '__main__':
    data = [
        (
            [1,2,3],
            [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]
        ),

    ]

    for item in data:
        nums, answer = item
        result = Solution().subset_recursion(nums)
        print(nums)
        print('Result:')
        print(result)
