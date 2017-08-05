function BinaryTreeNode(value) {
    this.depth = null;
    this.value = value;
    this.left = null;
    this.right = null;
    this.isLeaf = function() {
        return (this.left || this.right) ? false : true;
    };
}

var findRoot = function(hashMap) {
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
};

var createTree = function(data) {
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
};

var visit = function(node, visited) {
    if (visited[node.value]) {
        return visited;
    }

    if (node.depth === null) { node.depth = 0; } // root
    visited[node.value] = node;

    var queue = [];
    if (node.left && node.left.value)  { queue.push(node.left);  }
    if (node.right && node.right.value) { queue.push(node.right); }

    for(var i = 0; i<queue.length; i++) {
        queue[i].depth = node.depth + 1;
        visited = visit(queue[i], visited);
    }
    return visited;
};

var isSuperBalanced = function(root) {
    var visited = visit(root, {});

    var depthList = Object.keys(visited).reduce(function(result, key) {
        if (visited[key].isLeaf()) {
            result.push(visited[key].depth);
        }
        return result;
    }, []);

    return Math.max.apply(null, depthList) - Math.min.apply(null, depthList) <= 1;
};

// tests:
var assertEquals = function(a, b) {
    console.log(
        (a.toString() !== b.toString()) ? 'test fail: (' + a + ') !== (' + b + ')' : 'test pass.'
    );
};

// unit tests
(function() {
    var data = [[8,3,10], [3,1,6], [6,4,7], [10,null,14], [14, 13, null]];
    assertEquals(isSuperBalanced(createTree(data)), true);
})();

(function() {
    var data = [[8,3,10], [3,1,6], [6,4,7]];
    assertEquals(isSuperBalanced(createTree(data)), false);
})();


/*
 Write a function to see if a binary tree - is"superbalanced" (a new tree property we just made up).
 A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one.
*/