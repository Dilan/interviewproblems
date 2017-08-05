// Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

// For example, given n = 3, a solution set is:

/*
  ((()))
  (()())
  (())()
  ()(())
  ()()()
*/

var generateOneByOne = function(sublist, list, left, right) {
    if(left > right){
        return;
    }
    if(left > 0) {
        generateOneByOne( sublist + "(" , list, left-1, right);
    }
    if(right > 0) {
        generateOneByOne( sublist + ")" , list, left, right-1);
    }
    if(left == 0 && right == 0){
        list.push(sublist);
        return;
    }
}

var generateParenthesis = function(n) {
    var result = [];
    generateOneByOne('', result, n, n);
    return result;
}


var x = generateParenthesis(2);
console.log(x)
