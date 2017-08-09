var alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');

var startNodeId = "hit";
var endNodeId = "cog";
var dictionaryList = ["hit", "hot","dot","dog","lot","log","cog"];

var net = createNet(dictionaryList);
net.nodes[startNodeId].weight = 0;

start(startNodeId, net, endNodeId);

console.log("");
console.log("Shortest weight: " + net.findById(endNodeId).weight);
console.log("Path: " + findBackStep(endNodeId, net, startNodeId).reverse().join(' -> '));
console.log("");

// =============================================================================

function Node(id) {
    this.id = id;
    this.neighbors = [];
    this.visited = false;
    this.weight = Infinity;
};

function Net(id) {
    this.id = id;
    this.neighbors = [];
    this.visited = false;
    this.weight = Infinity;
}

function createNet(dictionaryList) {
    var net = new Net();

    var dict = {}
    dictionaryList.forEach(function(word) {
        dict[word] = true;
    });

    dictionaryList.forEach(function(id1) {
        get_neighbors(id1, dict).forEach((id2) => {
            var initNode = function(id, neighborId, weight) {
                var node, neighbor = new Neighbor(neighborId, weight);

                if(null == (node = net.findById(id))) {
                    node = net.createNode(id, neighbor);
                } else {
                    node.neighbors.push(neighbor);
                }
            };
            initNode(id1, id2, 1);
            initNode(id2, id1, 1);
        })
    });
    return net;
}

function get_neighbors(word, dict) {
    var neighbors = []
    get_all_possible_neighbors(word).forEach(key => {
        if(dict[key]) {
            neighbors.push(key);
        }
    });
    return neighbors;
}

function Neighbor(id, weight) {
    this.id = id;
    this.weight = weight;
}

function Net() {
    this.nodes = {};

    this.findById = function(id) {
        return (typeof this.nodes[id] == 'undefined') ? null : this.nodes[id];
    };

    this.createNode = function(id, neighbor) {
        this.nodes[id] = new Node(id);
        this.nodes[id].neighbors.push(neighbor);
        return this.nodes[id];
    };

    this.addVisibleButNotVisited= function(id) {
        if(this.visibleButUnVisited.indexOf(id) == -1) {
            this.visibleButUnVisited.push(id);
        }
    }

    this.visibleButUnVisited = [];
}

function get_all_possible_neighbors(word) {
    var keys = []
    word.split('').forEach(function(l, idx) {
        var mask = word.split('');
        alphabet.forEach(function(letter) {
            if (letter != l) {
                mask[idx] = letter
                keys.push(mask.join(''))
            }
        })
    })
    return keys
}

function start(nodeId, net, endNodeId) {
    Array.prototype.remove = function(member) {
        var index = this.indexOf(member);
        if(index > -1) {
            this.splice(index, 1);
        }
        return this;
    };

    net.visibleButUnVisited.remove(nodeId);

    net.findById(nodeId).visited = true;
    net.findById(nodeId).neighbors.forEach(function(neighbor) {
        var currentNode = net.findById(neighbor.id);
        if(!currentNode.visited) {
            if(Number(neighbor.weight) + Number(net.findById(nodeId).weight) < currentNode.weight) {
                currentNode.weight = Number(neighbor.weight) + Number(net.findById(nodeId).weight);
            }
            net.addVisibleButNotVisited(neighbor.id);
        }
    });

    var nodeWithSmallestWeight = { id:null, weight:Infinity };
    net.visibleButUnVisited.forEach(function(id) {
        if(Number(nodeWithSmallestWeight.weight) > Number(net.findById(id).weight)) {
            nodeWithSmallestWeight.id = net.findById(id).id;
            nodeWithSmallestWeight.weight = net.findById(id).weight;
        }
    });

    if(net.visibleButUnVisited.length) {
        start(nodeWithSmallestWeight.id, net, endNodeId);
    }
    return net;
}

function findBackStep(nodeId, net, startNodeId) {
    if(startNodeId == nodeId) { return [nodeId]; }

    var nextId, neighbor;
    for(var i=0; i < net.findById(nodeId).neighbors.length; i++) {
        neighbor = net.findById(nodeId).neighbors[i];
        if(net.findById(nodeId).weight - neighbor.weight == net.findById(neighbor.id).weight) {
            nextId = neighbor.id;
            break;
        }
    }
    return [nodeId].concat(findBackStep(nextId, net, startNodeId));
}
