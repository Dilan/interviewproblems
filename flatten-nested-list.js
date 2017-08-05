var solution = function(list) {
    return (function flat(list) {
        return list.reduce(function(result, item) {
            return result.concat((Array.isArray(item) ? flat(item) : [item]));
        }, []);
    })(list);
};

console.log(
    solution([1, [[2, [3, 4], 5, [6, [7]]]]])
);