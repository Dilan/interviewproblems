var getProductsOfAllIntsExceptAtIndex = function(list) {
    var tmp = 1, result = [];
    for(var i=0; i<list.length; i++) {
        result[i] = tmp;
        tmp = tmp * list[i];
    }
    tmp = 1;
    for(var i = list.length-1; i>=0; i--) {
        result[i] = result[i] * tmp;
        tmp = tmp * list[i];
    }
    return result;
};

var assertEquals = function(a, b) {
    console.log(
        (a.toString() !== b.toString()) ? 'test fail: (' + a + ') !== (' + b + ')' : 'test pass.'
    );
};

// unit tests
(function() {
    assertEquals([84, 12, 28, 21], getProductsOfAllIntsExceptAtIndex([1, 7, 3, 4]));
})();

/*
 You have an array of integers, and for each index you want to find the product of every integer except
 the integer at that index.
 Write a function getProductsOfAllIntsExceptAtIndex() that takes an array of integers and returns an array
 of the products.

 For example, given:

   [1, 7, 3, 4]

 your function would return:

   [84, 12, 28, 21]

 by calculating:

   [7*3*4, 1*3*4, 1*7*4, 1*7*3]

 Do not use division in your solution.
 */
