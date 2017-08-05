/**
 * collect max amount of coins jumping from [0] -> ... end of list
 * k - max jump length
 */
var solution = function(list, k) {
    var maxVal = function(index, l) {
        var r = [0];
        for(var i=1; i<=k; i++) {
            if (typeof l[index-i] !== 'undefined') {
                r.push(l[index-i]);
            }
        }
        return Math.max.apply(null, r);
    };
    var s = [];
    for(var i=0; i<list.length; i++) {
        s[i] = list[i] + maxVal(i, s);
    }
    console.log('Best for [' + list + '] is: ' + s[s.length-1]);
    return s;
};

solution([0, -2, 4, -7, 5, -2, -7, 9, 2, 0], 2);
solution([0, -2, 4, 0], 2);
solution([0, 3, -2, 4, -1, 0], 2);