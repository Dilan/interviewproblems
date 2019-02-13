# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5

class Solution(object):

    @staticmethod
    def partition(nums, start, end):
        pivot = start

        for i in range(start+1, end+1):
            if nums[i] < nums[start] and i >= 0 and i < len(nums):
                pivot += 1
                nums[i], nums[pivot] = nums[pivot], nums[i]
        nums[start], nums[pivot] = nums[pivot], nums[start]
        return pivot

    def findKthLargest(self, nums, k):
        start, end = (0, len(nums)-1)
        index = len(nums) - k

        while True:
            pivot = Solution().partition(nums, start, end)

            if pivot == index:
                break
            if index < pivot:
                start, end = start, (pivot - 1)
            else:
                start, end = (pivot + 1), end

        return nums[index]

# CLI
if __name__ == '__main__':

    k_nums_answer = [
        (5, [7,6,5,4,3,2,1],     3),
        (2, [3,2,1,5,6,4],       5),
        (4, [3,2,3,1,2,4,5,5,6], 4),
        (2, [2,1],               2),
    ]
    for data in k_nums_answer:
        k, nums, answer = data
        result = Solution().findKthLargest(nums, k)
        # print(result, nums)
        assert(answer == result)
