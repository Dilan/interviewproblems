var isBinarySearchTree = require('../InterviewCake-Problem-9').isBinarySearchTree;
var BinaryTreeNode = require('../InterviewCake-Problem-9').BinaryTreeNode;

// tests:

(function() {
    var data = [[8,3,10], [3,1,6], [6,4,7], [10,null,14], [14, 13, null]];
    assertEquals(isBinarySearchTree(createTree(data)), true);
})();

(function() {
    var data = [[8,3,10], [3,1,6], [6,4,5]];
    assertEquals(isBinarySearchTree(createTree(data)), false);
})();

(function() {
    var data = [[8,3,10], [3,1,6], [6,4,9]];
    assertEquals(isBinarySearchTree(createTree(data)), false);
})();

(function() {
    var data = [[50,30,80], [30,20,40], [80,60,90]];
    assertEquals(isBinarySearchTree(createTree(data)), true);
})();

function findRoot(hashMap) {
    var roots = {};
    var nonRoots = {};
    Object.keys(hashMap).map(function(key) {
        var node = hashMap[key];
        var left = node.left;
        var right = node.right;

        if (typeof nonRoots[node.value] === 'undefined') {
            roots[node.value] = true;
        }
        if (left !== null) {
            delete roots[left.value];
            nonRoots[left.value] = true;
        }
        if (right !== null) {
            delete roots[right.value];
            nonRoots[right.value] = true;
        }
    });
    return hashMap[Object.keys(roots)[0]];
}

function createTree(data) {
    var hm = {};
    for(var i=0; i < data.length; i++) {
        var value = data[i][0];
        var l = data[i][1];
        var r = data[i][2];

        var node;
        if (typeof hm[value] === 'undefined') {
            hm[value] = node = new BinaryTreeNode(value);
        } else {
            node = hm[value];
        }

        if (l) {
            if (typeof hm[l] === 'undefined') {
                hm[l] = new BinaryTreeNode(l);
            }
            node.left = hm[l];
        }
        if (r) {
            if (typeof hm[r] === 'undefined') {
                hm[r] = new BinaryTreeNode(r);
            }
            node.right = hm[r];
        }
    }
    return findRoot(hm);
}

function assertEquals(a, b) {
    console.log(
        (a.toString() !== b.toString()) ? 'test fail: (' + a + ') !== (' + b + ')' : 'test pass.'
    );
}