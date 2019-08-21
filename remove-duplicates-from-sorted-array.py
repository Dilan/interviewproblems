class Solution(object):
    def removeDuplicates(self, nums):

        if len(nums) == 0:
            return 0

        idx = 0
        for n in nums[1:]:
            if n > nums[idx]:
                idx += 1
                nums[idx] = n

        return idx + 1

if __name__ == "__main__":

    data = [
        ([1,1,2], [1,2]),
        ([0,0,1,1,1,2,2,3,3,4], [0,1,2,3,4]),
    ]

    for item in data:
        nums, answer = item
        result = Solution().removeDuplicates(nums)

        print(result == len(answer), result, answer, nums[0:result])
