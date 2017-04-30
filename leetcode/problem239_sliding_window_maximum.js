// https://leetcode.com/problems/sliding-window-maximum/

// Given an array nums, there is a sliding window of size k which is moving from 
// the very left of the array to the very right. You can only see the k numbers 
// in the window. Each time the sliding window moves right by one position.

// 
// For example,
// Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
// 
// Window position                Max
// ---------------               -----
// [1  3  -1] -3  5  3  6  7       3
//  1 [3  -1  -3] 5  3  6  7       3
//  1  3 [-1  -3  5] 3  6  7       5
//  1  3  -1 [-3  5  3] 6  7       5
//  1  3  -1  -3 [5  3  6] 7       6
//  1  3  -1  -3  5 [3  6  7]      7
// Therefore, return the max sliding window as [3,3,5,5,6,7].

var maxSlidingWindow = function(nums, k) {
    const deque = [];
    const result = [];

    for(let idx=0; idx<nums.length; idx++) {
        if (deque.length == k) { deque.shift(); }
        while(deque.length && nums[deque[deque.length-1]] < nums[idx]) {
            deque.pop();
        }
        deque.push(idx);
        if (idx >= k-1) {
            result.push(nums[deque[0]]);
        }
    }
    return result;
};

var assert = require('assert');
assert.deepEqual(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3), [3,3,5,5,6,7]);
assert.deepEqual(maxSlidingWindow([5,4,3,2,1,8,0], 2), [5,4,3,2,8,8]);

