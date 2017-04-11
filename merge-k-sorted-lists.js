/* 
    Merge k sorted linked lists and return it as one sorted list.
*/
function PriorityQueue() {
    this.heap = [];
    this.size = 0;
}

PriorityQueue.prototype = {
    get: function() {
        if (this.size === 0)
            return undefined;
        
        var out = this.heap[0];
        this.heap[0] = this.heap[this.size-1];
        delete this.heap[this.size-1];
        this.size --;
        
        var idx = 0;
        
        while(true) {
            var left = (idx<<1) + 1;
            var right = (idx<<1) + 2;
            var minIdx = idx;
            
            if (left < this.size && this.heap[idx][0] > this.heap[left][0]) {
                minIdx = left;
            }
            if (right < this.size && this.heap[minIdx][0] > this.heap[right][0]) {
                minIdx = right;
            }
            if (minIdx === idx) {
                break;
            }
            
            var tmp = this.heap[idx];
            this.heap[idx] = this.heap[minIdx];
            this.heap[minIdx] = tmp;
            idx = minIdx;
        }
        return out;
    },

    put: function(val, data) {
        
        var idx = this.size++;
        var parent = (idx - 1) >> 1;
        this.heap[idx] = [val, data];
        
        var tmp;
        while (idx > 0 && this.heap[parent][0] > this.heap[idx][0]) {
            tmp = this.heap[parent];
            this.heap[parent] = this.heap[idx];
            this.heap[idx] = tmp;
            idx = parent;
            parent = (idx-1)>>1;
        }
    }
}

function ListNode(val) {
    this.val = parseInt(val,10);
    this.next = null;
}

var mergeKLists = function(lists) {
    var q = new PriorityQueue();
    for (var i=0; i<lists.length; i++) {
        if (!lists[i]) continue;
        q.put(lists[i].val, lists[i]);
    }
    var root = new ListNode(null);
    var current = root;
    
    while (q.size) {
        var min_node = q.get()[1];
        current.next = min_node;
        
        if (min_node.next !== null) {
            q.put(min_node.next.val, min_node.next);
        }
        current = min_node;
    }
    return root.next;    
}

var toLinkedList = function(arr) {
    var root = new ListNode(arr[0]);
    var prev = root;
    for(var i=1; i<arr.length; i++) {
        var n = new ListNode(arr[i]);
        prev.next = n;
        prev = n; 
    }
    return root;
};

var toArray = function(root, list=[]) {
    if (root !== null) {
        list.push(root.val);
        toArray(root.next, list);
    }
    return list;
};

// 1st test --------------------------------------------------------------------
var assert = require('assert');

var result = mergeKLists([
    toLinkedList([7,26,40]),
    toLinkedList([2,5,30]),
    toLinkedList([60])
]);
assert.equal(toArray(result).toString(), '2,5,7,26,30,40,60')


// 2nd test --------------------------------------------------------------------
// read 10'000 lists
var data = JSON.parse(require('fs').readFileSync('./data/k-sorted-lists.v1.json', 'utf8'));
var kLists = data.map(arr => toLinkedList(arr));
var arr = toArray(mergeKLists(kLists));
assert.equal(arr.length, 10000);
assert.equal(arr[9999], 99);
assert.equal(arr[0], 0);

