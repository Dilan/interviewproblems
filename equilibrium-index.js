// The equilibrium index of a sequence is an index such that:
// the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

var A = [-1, 3, -4, 5, 1, -6, 2, 1];
var A_clone = A.slice(0);

var left_sum = A.map(function() { return 0; });
var right_sum = A.map(function() { return 0; });

for(var i = 1; i< A.length; i++) {
    left_sum[i] = left_sum[i-1] + A[i-1];
}

var result = [];
for(var j = (A.length-2); j>=0; j--) {
    right_sum[j] = right_sum[j+1] + A[j+1];
}

console.log(A_clone);
console.log(left_sum);
console.log(right_sum);
