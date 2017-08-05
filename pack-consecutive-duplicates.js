var myPack = function(list) {
    return list.slice(1).reduce(function(result, item) {
        if (result.prev === item ) {
            result.list[result.list.length - 1] += item;
        } else {
            result.prev = item;
            result.list.push(item)
        }
        return result;

    }, { prev: list[0], list: [list[0]] })['list']
};

console.log(
    myPack(['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e'])
);


/*
 Problem 9
 Pack consecutive duplicates of list elements into sublists.
 If a list contains repeated elements they should be placed in separate sublists.

 Example: myPack ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
 Should result: ['aaaa','b','cc','aa','d','eeee']
*/