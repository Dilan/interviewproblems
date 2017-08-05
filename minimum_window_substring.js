// Given a string S and a string T, find the minimum window in S which will contain 
// all the characters in T in complexity O(n).
// 
// For example,
// S = "ADOBECODEBANC"
// T = "ABC"
// Minimum window is "BANC".

var minWindow = function(s, t) {
    var seen = {};
    for (var i=0; i<t.length; i++) {
        seen[t[i]] = false;
    }
    
    var finished = {}
    var potentially = {}
    
    for (var i=0; i<s.length; i++) {
        
    }
    
    
    
    
};