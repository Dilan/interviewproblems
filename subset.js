var subset = function(list) {
    var results = [];
    var total = Math.pow(2, list.length)-1;
    for (var i=1; i<=total; i++) {
        var mask = i.toString(2);
        var result = [];
        var idx = 0;
        for (var j=mask.length-1; j>=0; j--) {
            if (mask[j] == '1') {
                result.push(list[idx])
            }
            idx++;
        }
        results.push(result);
    }
    return results
};

var x = subset(['a','b','c'])
console.log(x);

/*
var sets = (function(input, size) {
    var results = [], result, mask, i, total = Math.pow(2, input.length);
    for (mask = size; mask < total; mask++) {
        result = [];
        i = input.length - 1;

        do {
            if ((mask & (1 << i)) !== 0) {
                result.push(input[i]);
            }
        } while (i--);

        // if (result.length == size) {
            results.push(result);
        // }
    }

    return results; 
})(['a','b','c','d','e','f'], 0);
*/

// console.log(sets);