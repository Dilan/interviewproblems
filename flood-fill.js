// Flood fill, also called seed fill, is an algorithm that determines the area connected
// to a given node in a multi-dimensional array.
// It is used in the "bucket" fill tool of paint programs to fill connected,
// similarly-colored areas with a different color, and in games such as Go and Minesweeper
// for determining which pieces are cleared.
// When applied on an image to fill a particular bounded area with color, it is also
// https://en.wikipedia.org/wiki/Flood_fill

var area = [
    [1,1,1,1,0,0],
    [0,0,0,1,0,0],
    [1,1,1,1,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,1,1],
    [0,0,0,0,1,0]
];

var area_clone = area.map(function(item) { return item.slice(); });

var s = [4,2]; // point
var baseColor = 0;
var newColor = 5;

var neigbours = function(x,y, area) {
    var result = [];

    var conditions = [
        function(a,b) { return [a+1,b]; },
        function(a,b) { return [a-1,b]; },
        function(a,b) { return [a,b+1]; },
        function(a,b) { return [a,b-1]; }
    ];

    conditions.forEach(function(item) {
        var xy = item(x,y);
        if (typeof area[xy[0]] !== 'undefined' &&
            typeof area[xy[0]][xy[1]] !== 'undefined')
        {
            result.push([xy[0], xy[1]]);
        }
    });

    return result;
};

var queue = [s];

while(queue.length) {
    var node = queue.pop();

    var x = node[0];
    var y = node[1];

    if(area[x][y] == baseColor) {
        area[x][y] = newColor;
    }

    var neighbourList = neigbours(node[0], node[1], area);
    neighbourList.forEach(function(item) {
        if (area[item[0]][item[1]] == baseColor) {
            queue.push(item);
        }
    });
}

console.log('Before:');
console.log(area_clone);
console.log('Click to', s);
console.log('After:');
console.log(area);