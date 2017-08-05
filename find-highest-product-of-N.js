/*
 Given an arrayOfInts, find the highestProduct you can get from (N) of the integers.

 The input arrayOfInts will always have at least N integers.
*/
var addIfBigEnough = function(item, sortedList, maxLength, sortFunct) {
    sortedList.push(item);
    sortedList.sort(sortFunct || function(a, b) {
        return item > 0 ? (a - b) : (b - a);
    });
    return sortedList.slice(-maxLength);
};

var product = function() {
    return function(prev, item) {
        return prev * item;
    };
};

var solution = function(list, n) {
    var result = list.reduce(function(result, item) {
        var property = (item > 0 ? 'maxPositive' : 'minNegative');
        result[property] = addIfBigEnough(item, result[property], n);

        if (item < 0 && result['maxPositive'].length === 0) {
            result['maxNegative'] = addIfBigEnough(item, result['maxNegative'], n, function(a, b) { return (a - b); });
        }
        return result;
    }, { maxPositive: [], minNegative: [], maxNegative: [] });

    // console.log(result);

    // maxPositive & minNegative
    if (result['maxPositive'].length > 0) {
        var l = [];
        while(l.length < n) {
            var n1 = result['minNegative'].pop();
            var n2 = result['minNegative'].pop();
            var p1 = result['maxPositive'].pop();
            var p2 = result['maxPositive'].pop();

            if (typeof n1 === 'undefined' || typeof n2 === 'undefined') {
                l.push(p1);
                l.push(p2);
            } else if (typeof p1 === 'undefined' || typeof p2 === 'undefined') {
                l.push(n1);
                l.push(n2);
            } else if (p1 * p2 > n1 * n2) {
                l.push(p1);
                l.push(p2);
                result['minNegative'].push(n2);
                result['minNegative'].push(n1);
            } else {
                l.push(n1);
                l.push(n2);
                result['maxPositive'].push(p2);
                result['maxPositive'].push(p1);
            }
            if ((n % 2) && l.length === n - 1) {
                l.push(result['maxPositive'].pop());
                break;
            }
        }
        return l.reduce(product(), 1);

    } else {
        return result.maxNegative.reduce(product(), 1);
    }
};

var assertEquals = function(a, b) {
    console.log(
        (a.toString() !== b.toString()) ? 'test fail: (' + a + ') !== (' + b + ')' : 'test pass.'
    );
};

// unit tests
(function() {
    assertEquals(
        [10, -5, 2, -100].reduce(product(), 1),
        solution([1, 10, -5, 1, 1, 2, -100], 4)
    );
})();

(function() {
    assertEquals(
        [-1, -2, -3].reduce(product(), 1),
        solution([ -1, -2, -3, -4, -5, -6], 3)
    );
})();

(function() {
    assertEquals(
        [-9, -8, 7].reduce(product(), 1),
        solution([1,2,3,4,-9,-6,-1,8,-7], 3)
    );
})();

(function() {
    assertEquals(
        [-40, -50, -60, -70].reduce(product(), 1),
        solution([-10, -20 , -30 , -40, -50, -60, -70, 1, 2, 4], 4)
    );
})();

(function() {
    assertEquals(
        [-40, -50, -60, -70, 4].reduce(product(), 1),
        solution([-10, -20 , -30 , -40, -50, -60, -70, 1, 2, 4], 5)
    );
})();
