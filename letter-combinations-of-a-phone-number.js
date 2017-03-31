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
        '0': ''
    };
    return hm[digit].split('');
};

var letterCombinations = function(digits) {
    digits = digits.toString().split('');
    
    if (digits.length === 0) {
        return [];
    }
    
    var result = letters(digits.shift());
    while (digits.length > 0) { 
        var ls = letters(digits.shift());
        var tmp = [];
        for(var i = 0; i < result.length; i++) {
            for(var j=0; j < ls.length; j++) {
                tmp.push(result[i] + ls[j]);
            }
        }
        result = tmp;
    }
    return result;
};

var result = letterCombinations('23');
console.log(result);