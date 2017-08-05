// Find the sum of k largest integers in array

function MinHeap() {
    this.heap = [];
    this.size = 0;
}
MinHeap.prototype.get = function() {
    var out = this.heap[0];
    
    this.heap[0] = this.heap.pop();
    this.size--;
 
    var left, right, nextIdx, idx=0;
    while(true) {
        left = (idx << 1) + 1;
        right = (idx << 1) + 2;
        
        nextIdx = idx;
        if (this.heap[left] < this.heap[idx]) {
            nextIdx = left;
        }
        if (this.heap[right] < this.heap[nextIdx]) {
            nextIdx = right;
        }
        
        if (idx === nextIdx) {
            break;
        }
            
        var tmp; // swap
        tmp = this.heap[nextIdx];
        this.heap[nextIdx] = this.heap[idx];
        this.heap[idx] = tmp;
        
        idx = nextIdx;
    }
    
    return out;
};

MinHeap.prototype.put = function(val) {
    var tmp, idx = this.size++;
    this.heap[idx] = val;
    
    while(idx > 0) {
        var parentIdx = idx >> 1;
        
        if (this.heap[parentIdx] <= this.heap[idx]) {
            break;
        }
        // swap
        tmp = this.heap[parentIdx];
        this.heap[parentIdx] = this.heap[idx];
        this.heap[idx] = tmp;
        idx = parentIdx;
    }
}

var solution = function(list, k) {
    var mHeap = new MinHeap();
    mHeap.put(3);
    mHeap.put(5);
    mHeap.put(9);
    mHeap.put(2);
    mHeap.put(1);
    mHeap.put(10);
    mHeap.put(7);
    mHeap.put(8);
    mHeap.put(12);
    
    console.log(mHeap.heap);
    
    console.log(mHeap.get());
    console.log(mHeap.heap);
    console.log(mHeap.get());
    console.log(mHeap.heap);
    console.log(mHeap.get());
    console.log(mHeap.heap);
    
    console.log(mHeap.get());
    console.log(mHeap.heap);
    
};


var list = [5,2,7,9];
var result = solution(list)