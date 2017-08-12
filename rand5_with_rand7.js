/*
 You have a function rand7() that generates a random integer from 1 to 7.
 Use it to write a function rand5() that generates a random integer from 1 to 5.

 rand7() returns each integer with equal probability.
 rand5() must also return each integer with equal probability.
*/

var rand7 = function() {
    return Math.floor(1 + Math.random() * 7)
};

var rand5 = function() {
    while(true) {
        var r = rand7();
        if (r <= 5) {
            return r;
        }
    }
};

module.exports.rand5 = rand5;
