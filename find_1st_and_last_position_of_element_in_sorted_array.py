# Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

class Solution(object):
    def searchRange(self, nums, target):
        # binary search
        start, end = 0, len(nums)-1
        while start <= end:
            mdx = (start + end) >> 1
            middle = nums[mdx]

            if target == middle:
                return Solution.find_equal_range(nums, mdx)

            if target > middle:
                start = mdx + 1
            else:
                end = mdx - 1

        return [-1,-1]

    @staticmethod
    def find_equal_range(nums, idx):
        the_range = [idx, idx]
        val = nums[idx]

        to_left = lambda x: x-1 if x >= 0 else -1
        to_right = lambda x: x+1 if x+1 < len(nums) else -1

        for i,move in enumerate([to_left, to_right]):
            ndx = idx
            while True:
                ndx = move(ndx)
                if ndx == -1 or val != nums[ndx]:
                    break
                if val == nums[ndx]:
                    the_range[i] = ndx

        return the_range


if __name__ == '__main__':
    data = [
        # ([5,5], 5, [0,1]),
        ([5], 5, [0,0]),
        # ([5,7,7,8,8,10], 8, [3,4]),
        # ([5,7,7,8,8,10], 6, [-1,-1]),
    ]

    for items in data:
        nums, target, output = items
        result = Solution().searchRange(nums, target)

        print('Answer vs Result', output, result)
