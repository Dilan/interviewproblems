// Given the array of IDs, which contains many duplicate integers and one unique integer, find the unique integer.

module.exports.findUnique = function(list) {
    var hm = {
        counter: { },
        unique: { }
    };
    for (var i=0; i<list.length; i++) {
        var item = list[i];

        if (typeof hm.counter[item] === 'undefined') {
            hm.counter[item] = 0;
            hm.unique[item] = true;
        }
        hm.counter[item] += 1;

        if (hm.counter[item] > 1) {
            delete hm.unique[item];
        }
    }
    return Object.keys(hm.unique)[0];
};