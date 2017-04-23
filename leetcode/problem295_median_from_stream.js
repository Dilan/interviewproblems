// https://leetcode.com/problems/find-median-from-data-stream/

// Median is the middle value in an ordered integer list. 
// If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
// Examples: 
// [2,3,4] , the median is 3
// [2,3], the median is (2 + 3) / 2 = 2.5

var addToSortedList = (num, list) => {
    var [low, high] = [0, list.length];
    while (low < high) {
        let m = (high + low) >> 1;
        if (num > list[m]) low = m + 1;
        else high = m;
    }
    list.splice(low, 0, num);
}

var MedianFinder = function() {
    this.list = [];
    this.length = 0;
};

MedianFinder.prototype.addNum = function(num) {
    addToSortedList(num, this.list);
    this.length++;
    return this;
};

MedianFinder.prototype.findMedian = function() {
    if (this.length % 2 === 0) {
        var a = this.list.length / 2;
        var b = a - 1;
        return (this.list[a] + this.list[b]) / 2;
    } else {
        return this.list[(this.list.length >> 1)];
    }
};

const assert = require('assert');

var obj = new MedianFinder();
obj.addNum(2).addNum(1).addNum(6).addNum(9).addNum(5).addNum(3); // => [1,2,3,5,6,9]

assert.equal(obj.findMedian(), 4)

obj.addNum(12); // => [1,2,3,5,6,9,12]
assert.equal(obj.findMedian(), 5);
