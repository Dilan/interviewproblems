var solution = function(list) {
    var roots = {};
    var notRoots = {};
    var net = list.reduce(function(result, item) {
        var node = { id: item[0] };
        var neighbor = { id: item[1] };

        if (!notRoots[node.id]) {
            roots[node.id] = 1;
        }
        if (roots[neighbor.id]) {
            delete roots[neighbor.id];
        }
        notRoots[neighbor.id] = 1;

        if (typeof result[node.id] === 'undefined') {
            var neighbors = {};
            neighbors[neighbor.id] = neighbor;
            result[node.id] = { neighbors: neighbors };
        } else {
            result[node.id].neighbors[neighbor.id] = neighbor;
        }

        return result;

    }, {});

    for(var i=0; i<Object.keys(net).length; i++) {
        // var v = net[i]
    }

};

solution([
    [1, 2],
    [1, 3],
    [2, 4],
    [3, 2],
    [3, 4]
]);