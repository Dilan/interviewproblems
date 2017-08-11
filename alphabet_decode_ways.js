// https://leetcode.com/problems/decode-ways/description/

// Given the alphabet encoded as numbers (e.g., a=1, b=2, ..., z=26), 
// and a sequence of numbers (e.g., "23413259802"), 

// How many strings can be generated?

var alphabet = function() {
    var list = [undefined];
    for (var i = 'a'.charCodeAt(0); i<='z'.charCodeAt(0); i++) {
        list.push(String.fromCharCode(i));
    }
    return list;
};
var az = alphabet();

var toLetter = function(num) {
    num = parseInt(num,10);
    return az[num];
};

var generateString = function(nums, i, substr, result) {
    if (i >= nums.length) {
        result.push(substr);
        return;
    }
    generateString(nums, i+1, substr + toLetter(nums[i]), result);
    
    if (typeof nums[i+1] !== 'undefined' && parseInt(nums[i]+nums[i+1], 10) < 27) {
        generateString(nums, i+2, substr + toLetter(nums[i]+nums[i+1]), result);
    }
};

var solution = function(numbers) {
    numbers = numbers.toString();
    var result = [];
    generateString(numbers, 0, '', result);
    return result;
};

var note = '';
for (var i=1; i<az.length; i++) {
    note += i + ':' + az[i] + ' ';
}

var assert = require('assert');
assert.deepEqual(solution(214), [ 'bad', 'bn', 'ud' ]);
