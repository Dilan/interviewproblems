/* 
    Given an integer array A find all the complementary pairs in A 
    that sums up to a provided value K, so for example given the array [2, 5, -1, 6, 10, -2] 
    and an integer K = 4 the result must be 5 because the input array contains 
    [2, 2] [5, -1] [-1, 5] [6, -2] [-2, 6]
    The solution is expected to run with a total time complexity of O(N logN)
*/

var solution = function(k, list) {
    var hm = list.reduce(function(hm, item) {
        if (typeof hm[item] == 'undefined') {
            hm[item] = 0;
        }
        hm[item]++;
        return hm;
    }, {});
    
    var counter = 0;
    list.forEach(function(item) {
        var rest = k - item;
        if (typeof hm[rest] !== 'undefined') {
            counter += hm[rest];
        }
    });
    return counter;
};

var args = process.argv.slice(2);

try {
    if (args[0] && args[1]) {
        var answer = solution(parseInt(args[0]), JSON.parse(args[1]));
        console.log('Answer:', answer);
    } else {
        var answer = solution(6, [1, 8, -3, 0, 1, 3, -2, 4, 5]);
        console.log('Answer:', answer);
        
    }
} catch(err) {
    console.log('Error:', err.stack);
}
