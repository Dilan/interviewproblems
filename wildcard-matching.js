// '?' Matches any single character.
// '*' Matches any sequence of characters (including the empty sequence).

// The matching should cover the entire input string (not partial).

// The function prototype should be:
// bool isMatch(const char *s, const char *p)

// Some examples:
// isMatch("aa","a") → false
// isMatch("aa","aa") → true
// isMatch("aaa","aa") → false
// isMatch("aa", "*") → true
// isMatch("aa", "a*") → true
// isMatch("ab", "?*") → true
// isMatch("aab", "c*a*b") → false

var isMatch = function(s, p) {
    
    var lastPattern = p[0];
    
    for (var i=0; i<s.length; i++) {
        var c1 = s[i];
        var c2 = p[i];
        
        if (c2 !== lastPatter n) {
            lastPattern = c2;
        }
        
        if (c2 === '?' || c1 === c2) {
            continue;
        }
        if (lastPattern == '*')
    }
    return true;
    
};
