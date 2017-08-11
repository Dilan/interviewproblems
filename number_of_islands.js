// https://leetcode.com/problems/number-of-islands/description/
// Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.

// 11000
// 11000
// 00100
// 00011

// Answer: 3

// An island is surrounded by water and is formed by connecting adjacent lands
// horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

var toGrid = function(input) {
    return input.map(function(str) {
        return str.split('');
    });
};

var numIslands = function(grid) {
    var seen = []
    for (var i=0; i < grid.length; i++) {
        var row = grid[i];
        seen.push(row.slice().map(function(x) {
            return false;
        }));
    }

    var islandCounter = 0;
    var walk = function(x,y) {
        seen[x][y] = true;

        var move = {
            'up':    function(x,y) { return [x,y-1]; },
            'down':  function(x,y) { return [x,y+1]; },
            'left':  function(x,y) { return [x-1,y]; },
            'right': function(x,y) { return [x+1,y]; }
        }

        var ways = [move.up,move.down, move.left, move.right];
        for(var i=0; i<ways.length; i++) {
            var m = ways[i];
            var point = m(x,y);
            var px = point[0];
            var py = point[1];
            if (typeof seen[px] !== 'undefined' &&
                !seen[px][py] &&
                typeof grid[px] !== 'undefined' &&
                grid[px][py] === '1')
            {
                walk(px, py);
            }
        }
        return;
    };

    var isVisited = function(x,y) {
        return seen[x][y];
    };
    for (var i=0; i < grid.length; i++) {
        var row = grid[i];
        for (var j=0; j < row.length; j++) {
            if (seen[i][j]) {
                continue;
            }
            var isLand =  grid[i][j] === '1'  ? true : false;
            if (isLand) {
                islandCounter ++;
                walk(i,j);
            }
        }
    }
    return islandCounter;
};

// Unit Tests ------------------------------------------------------------------
var assert = require('assert');

assert.equal(
    3,
    numIslands(
        toGrid([
            '11000',
            '11000',
            '00100',
            '00011'
        ])
    )
);
assert.equal(
    1,
    numIslands(
        toGrid([
            '11110',
            '11010',
            '11000',
            '00000'
        ])
    )
);
