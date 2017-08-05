var minWindow = function(s, t) {
    var need = t.split('').reduce(function(prev, item) {
        prev[item] = 1;
        return prev;
    }, {});
    var missing = t.length;
    var i = I = J = 0;
    
    for(var x=0; x<s.length; x++) {
        var j = x + 1;
        var c = s[x];
        need[c] = (typeof need[c] == 'undefined' ) ? -1 : (need[c]-1);
        missing -= (need[c] == 0 ? 1: 0);
        
        if (missing <= 0) {
            while ( i<j && need[s[i]] < 0) {
                need[s[i]] += 1;
                i++
            }
            if (j-i <= J-I || J == 0) {
                I = i;
                J = j;
            }
        }
    }
    return s.slice(I,J);
};

var result = minWindow('AXXBCXXXXBAC', 'ABC');
console.log(result)
