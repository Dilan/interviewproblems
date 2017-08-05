// https://leetcode.com/problems/repeated-dna-sequences/description/

// All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, 
// for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

// Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

// For example:
// var s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
// ["AAAAACCCCC", "CCCCCAAAAA"]

function Storage() {
    this.hashmap = {};
    this.moreThanOnce = [];    
}

Storage.prototype.add = function(str) {
    if (typeof this.hashmap[str] === 'undefined') {
        this.hashmap[str] = 1;
    } else {
        if (this.hashmap[str] === 1) {
            this.moreThanOnce.push(str);
        }
        this.hashmap[str] += 1;
    }
};

var findRepeatedDnaSequences = function(str, k=10) {
    var result = [];
    var storage = new Storage()
    
    var sequences = '';
    var start = 0;
    for (var i=k; i<=str.length; i++) {
        sequences = str.substr(start, k);
        if (sequences.length < k) { break; }
        storage.add(sequences);
        start ++;
    }
    return storage.moreThanOnce;
};

// Unit Tests ------------------------------------------------------------------
var assert = require('assert');

assert.deepEqual(
    findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'), 
    ['AAAAACCCCC', 'CCCCCAAAAA']
);

assert.deepEqual(
    findRepeatedDnaSequences('AAAAAAAAAAA'), 
    ['AAAAAAAAAA']
);
