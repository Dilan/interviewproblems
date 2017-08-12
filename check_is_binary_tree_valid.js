/*
 Write a function to check that a binary tree ↴ is a valid binary search tree ↴ .
 Here's a sample binary tree node class:
*/
var apply = function(func, a, b) {
    if (typeof a === 'undefined' && typeof b === 'undefined') {
        return undefined;
    }
    return func.apply(null,[]
            .concat(typeof a !== 'undefined' ? [a] : [])
            .concat(typeof b !== 'undefined' ? [b] : [])
    );
};

var isBinaryTreeNode = function(value, min, max) {
    return ((typeof min === 'undefined' || value >= min) &&
        (typeof max === 'undefined' || value <= max));
};

var isBinarySearchTree = function(node, options) {
    options = options || {};
    var left = node.left;
    var right = node.right;
    var queue = [];

    if (left !== null) {
        if (false === isBinaryTreeNode(left.value,
                options['min'],
                apply(Math.min, node.value, options['max'])))
        {
            return false;
        }
        queue.push({
            node: left, options: { min: options['min'], max: node.value }
        });
    }
    if (right !== null) {
        if (false === isBinaryTreeNode(right.value,
                apply(Math.max, node.value, options['min']),
                options['max']))
        {
            return false;
        }
        queue.push({
            node: right, options: { min: node.value, max: options['max'] }
        });
    }

    for(var i = 0; i < queue.length; i++) {
        if (false === isBinarySearchTree(queue[i].node, queue[i].options)) {
            return false;
        }
    }
    return true;
};
module.exports.isBinarySearchTree = isBinarySearchTree;

module.exports.BinaryTreeNode = function(value) {
    return {
        value: value,
        left: null,
        right: null
    }
};
