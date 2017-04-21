// Given a digit string, return all possible letter combinations that the number could represent.
// A mapping of digit to letters (just like on the telephone buttons) is given below.

// =============================================================================
//  1       2 abc    3 def
//  4 ghi   5 jkl    6 mno
//  7 pqrs  8 tuv    9 wxyz
//          0
// =============================================================================

// Input:Digit string "23"
// Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

var letters = function(digit) {
    var hm = {
        '1': '',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ' '
    };
    return hm[digit].split('');
};

var letterCombinations = (str, k, result) => {
    if (str.length-1 < k) {
        return;
    }
    var chars = [...letters(str[k])];
    
    if (k === 0) {
        result.splice(0, 0, ...chars);
    } else {
        var len = result.length;
        var next = len;
        for(var j=0; j<len; j++) {
            var tmp = result[j];
            for(var i=0; i<chars.length; i++) {
                result[ (i === 0 ? j : next++)  ] = tmp + chars[i];
            }
        }
    }
    letterCombinations(str, k+1, result);
};

var solution = (val) => {
    var result = [];
    letterCombinations(val, 0, result);
    return result;
};

var assert = require('assert');
assert.equal(solution('23').toString(), 'ad,bd,cd,ae,af,be,bf,ce,cf');
assert.equal(solution('90').toString(), 'w ,x ,y ,z ');
