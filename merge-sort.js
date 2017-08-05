var merge = function(a, b) {
    var result = [];
    while(a.length || b.length) {
        if (a.length == 0 || b.length == 0) {
            result = result.concat(
                (b.length == 0) ? a : b
            );
            break;
        } else {
            result.push(
                (a[0] <= b[0] ? a.shift() : b.shift())
            );
        }
    }
    return result;
};
var divide = function(list) {
    var middleIndex = (list.length / 2) | 0;
    return [list.slice(0, middleIndex), list.slice(middleIndex)]; // left / right
};

var mergeSort = function(list) {
    var r = divide(list);
    var left = r[0];
    var right = r[1];

    if (left.length <= 1 && right.length <=1) {
        return merge(left, right);
    } else {
        return merge(mergeSort(left), mergeSort(right));
    }
};

var assertEqual = function(a, b) {
    return console.log(
        ((a === b) ? '[done]' : a + '\n' + b + '\n are not equal')
    );
};
// tests:
assertEqual(
    [1,2,3].toString(),
    mergeSort([3,2,1]).toString()
);

assertEqual(
    [1,2,3,4,5,6,7,8].toString(),
    mergeSort([6,5, 3,1, 8,7, 2, 4]).toString()
);
