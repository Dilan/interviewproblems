// https://leetcode.com/problems/permutations-ii

// Given a collection of numbers that might contain duplicates, return all possible unique permutations.

// For example [1,1,2] have the following unique permutations:
// [ [1,1,2], [1,2,1], [2,1,1] ]

const permuteUnique = (nums, k=0, result=[]) => {
    if (k >= (nums.length)) {
        result.push(nums.slice());
        return;
    }    
    for(let i=k; i<nums.length; i++) {
        if (i !== k && nums[i] === nums[k]) continue; // skip useless swap
        [nums[i], nums[k]] = [nums[k], nums[i]];
        permuteUnique(nums, k+1, result);
        [nums[k], nums[i]] = [nums[i], nums[k]];
    }
    
    return result;
};

var assert = require('assert');
assert.deepEqual(permuteUnique([1,2,1]), [[1,2,1],[1,1,2],[2,1,1]]);
assert.deepEqual(permuteUnique([1,1,1]), [[1,1,1]]);
