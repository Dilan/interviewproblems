(function(graph, startNodeId, endNodeId) {

    Array.prototype.remove = function(member) {
        var index = this.indexOf(member);
        if(index > -1) {
            this.splice(index, 1);
        }
        return this;
    };

    var Node = function(id) {
        this.id = id;
        this.neighbors = [];

        this.visited = false;
        this.weight = Infinity;
    };

    var Neighbor = function(id, weight) {
        this.id = id;
        this.weight = weight;
    };

    var Net = function() {
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
    };

    var createNet = function(graph, startNodeId) {
        var net = new Net();

        graph.forEach(function(data) {

            var id1 = data[0];
            var id2 = data[1];
            var weight = data[2];

            var initNode = function(id, neighborId, weight) {
                var node, neighbor = new Neighbor(neighborId, weight);

                if(null == (node = net.findById(id))) {
                    node = net.createNode(id, neighbor);
                    if(startNodeId == id) {
                        node.weight = 0;
                    }
                } else {
                    node.neighbors.push(neighbor);
                }
            };

            initNode(id1, id2, weight);
            initNode(id2, id1, weight);
        });

        return net;
    };

    var start = function(nodeId, net, endNodeId) {

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
    };



    var findBackStep = function(nodeId, net, startNodeId) {
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
    };

    var net = start(startNodeId, createNet(graph, startNodeId), endNodeId);

    console.log("");
    console.log("Shortest weight: " + net.findById(endNodeId).weight);
    console.log("Path: " + findBackStep(endNodeId, net, startNodeId).reverse().join(' -> '));
    console.log("");

})([['A','B','6'],
    ['A','D','18'],
    ['A','C','3'],
    ['B','D','11'],
    ['B','E','5'],
    ['C','D','20'],
    ['C','F','10'],
    ['D','E','13'],
    ['D','F','1'],
    ['D','G','17'],
    ['E','G','9'],
    ['F','G','14']],
    'A', 'G'
);

/*
for example:

            5
        B ------- E
     6 /     13 /   `. 9
      /  18    /  17  `.
     A ----- D -------- G
      \    /20 `. 1    /
    3 \   /      `.   / 14
       C ---------- F
            10
 */