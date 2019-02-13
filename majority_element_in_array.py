# Given an array of size n, find the majority element.
# The majority element is the element that appears more than n/2 times.
# You may assume that the array is non-empty and the majority element always exist in the array.

class Solution(object):
    # O(n) - time complexity
    # O(n) - additional space
    def majorityElement(self, nums):
        counters = {}
        for i,n in enumerate(nums):
            if n not in counters:
                counters[n] = 1
            else:
                counters[n] += 1

        result = 0
        value = 0
        for k in counters:
            if result < counters[k]:
                value = k
                result = counters[k]

        return value

print(Solution().majorityElement([1,1,2,2,2]))
print(Solution().majorityElement([1,1,2,1,2]))
