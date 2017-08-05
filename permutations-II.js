// Given a collection of numbers that might contain duplicates, return all possible unique permutations.

// For example,
// [1,1,2] have the following unique permutations:

var walkInArray = function(item, list) {
    var result = [];
    for (var i=0; i<=list.length; i++) {
        if (i==0 || (i > 0 && item !== list[i-1])) {
            result.push( list.slice(0,i).concat([item], list.slice(i)));
        }
    }
    return result;
}
var permutations = function(list) {
    if (list.length <= 1) {
        return [list];
    }
    var firstItem = list[0];
    var result = [];
    permutations(list.slice(1)).forEach(function(perm) {
        walkInArray(firstItem, perm).forEach(function(new_perm) {
            result.push(new_perm);
        });
    });
    return result;
};

var swap = function(a, b, list) {
    var tmp = list[a];
    list[a] = list[b];
    list[b] = tmp;
}

var permutation_inplace = function(a, k=0, result=[]) {
    
    if (k == a.length) {
        return result.push(a.slice())
    }
    for (var i=k; i<a.length; i++) {
        if (i != k && a[i] == a[k]) continue;
        swap(k, i, a);
        permutation_inplace(a, k+1, result)
        swap(i, k, a);
    }
    return result;
}

var x = permutation_inplace([1,1,3]);
console.log(x);

var x = permutations([1,1,3]);
console.log(x);


// var result = permutations([1,2,1]);
// var result = permutations([1,2,3]);
// console.log(result);