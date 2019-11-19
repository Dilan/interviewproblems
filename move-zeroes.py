"""
Given an array nums, write a function to move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, z = 0, None
        while i < len(nums):

            if nums[i] == 0:
                if z is not None:
                    z = min(i, z)
                else:
                    z = i
            else:
                if z is not None:
                    nums[i], nums[z] = nums[z], nums[i]
                    z = z + 1

            i += 1

if __name__ == '__main__':
    data = [
        ([0,1,0,3,12], [1,3,12,0,0]),

    ]

    for item in data:

        input, answer = item
        result = Solution().moveZeroes(input)

        print(input, answer)
