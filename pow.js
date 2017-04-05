var myPow = function(x, n) {
    if (n === 0) {
        return 1;
    }
    if (x == -1) {
        return Math.abs(n)%2 === 0 ? 1 :-1;
    }
    result = x;
    var nn = Math.abs(n) - 1;
    var prev = x;
    while (nn > 0) {
        result *= x;
        nn--;
        if (prev == result ||
            (result > 100000 && n<0) ||
            (result > 0 && n>0 && result < (1/1000000))) 
        {
            break;
        }
    }
    
    if (n < 0) {
        result = 1 / result
    }
    if (result < (1/100000) && result > 0) {
        result = 0.0
    }
    return result;
};

var assert = require('assert');
assert.equal(Math.pow(2.00000,-2147483648), myPow(2.00000,-2147483648));
assert.equal(Math.pow(-3.39758,5), myPow(-3.39758,5));
assert.equal(Math.pow(0.00001, 2147483647), myPow(0.00001, 2147483647));
assert.equal(Math.pow(1.0, -214748), myPow(1.0, -214748));
assert.equal(Math.pow(-1.0, -214748), myPow(-1.0, -214748));
