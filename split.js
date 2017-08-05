var split = function(str, delimiter) {
    var result = [];

    var tmp = '';
    for(var i=0; i<str.length; i++) {
        if (str[i] !== delimiter) {
            tmp += str[i];
        } else {
            result.push(tmp);
            tmp = '';
        }
    }

    if (tmp.length) {
        result.push(tmp);
    }

    return result;
};

console.log(split('a-bb-ccc', '-'));