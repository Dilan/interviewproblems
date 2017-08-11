var startNodeId = "hit";
var endNodeId = "cog";
var dictionaryList = ["hit", "hot","dot","dog","lot","log","cog"];
var result = findLadders(startNodeId, endNodeId, dictionaryList);
console.log(result);

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

    var hmask = {}
    dictionaryList.forEach(function(word) {
        var k, mask = word.split('');
        mask.forEach(function(l, idx) {
            mask[idx] = '*';
            k = mask.join('');
            if (typeof hmask[k] == 'undefined') {
                hmask[k] = [word];
            } else {
                hmask[k].push(word);
            }
            mask[idx] = l;
        });
    });

    var initNode = function(id, neighborId, weight) {
        var node, neighbor = new Neighbor(neighborId, weight);

        if(null == (node = net.findById(id))) {
            node = net.createNode(id, neighbor);
        } else {
            node.neighbors.push(neighbor);
        }
    };

    var dict = {}
    Object.keys(hmask).forEach(m => {
        var neighbors = hmask[m]
        var id1, id2;
        for(var i=0; i<neighbors.length; i++) {
            id1 = neighbors[i];
            for(var j=i+1; j<neighbors.length; j++) {
                id2 = neighbors[j]
                initNode(id1, id2, 1);
                initNode(id2, id1, 1);
            }
        }
    });
    return net;
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

function findBackStepList(nodeId, net, startNodeId, path=[], result=[]) {
    path.push(nodeId);

    if (nodeId == startNodeId) {
        return result.push(path);
    } else if (!net.findById(nodeId)) {
        return [];
    }

    for(var i=0; i < net.findById(nodeId).neighbors.length; i++) {
        neighbor = net.findById(nodeId).neighbors[i];
        if(net.findById(nodeId).weight - neighbor.weight == net.findById(neighbor.id).weight) {
            findBackStepList(neighbor.id, net, startNodeId, path.slice(), result);
        }
    }
    return result;
}

function findLadders(beginWord, endWord, wordList) {
    var net = createNet(wordList);
    net.nodes[beginWord].weight = 0;
    start(beginWord, net, endWord);
    return findBackStepList(endWord, net, beginWord).map(function(list) {
        return list.reverse();
    });
};
