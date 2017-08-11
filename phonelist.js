/*
    https://cmind.kattis.com/problems/phonelist

    Given a list of phone numbers, determine if it is consistent in the sense
    that no number is the prefix of another. Let’s say the phone catalogue listed these numbers:

    Emergency 911
    Alice 97 625 999
    Bob 91 12 54 26

    In this case, it’s not possible to call Bob, because the central would direct
    your call to the emergency line as soon as you had dialled the first three
    digits of Bob’s phone number. So this list would not be consistent.
*/

function Node(val) {
    this.val = val;
    this.children = null;
}

var solution = function(list) {
    var hm = {};
    for(var j=0; j<list.length; j++) {
        var phone = list[j];
        var root = hm;
        for(var i=0; i<phone.length; i++) {
            var n = phone[i];
            var isLast = (i == (phone.length-1));

            if (typeof root[n] == 'undefined') {
                root[n] = new Node(n);
                if (isLast == false) {
                    root[n].children = {};
                }
                root = root[n];

            } else if (root[n].children == null || isLast == true) {
                return false;

            } else {
                root = root[n];
            }
        }
    }
    return true;
};

// tests:
var assert = require('assert');
assert.equal(
    true,
    solution([
        '113',
        '12340',
        '123440',
        '12345',
        '98346'
    ])
);
assert.equal(
    false,
    solution([
        '911',
        '97625999',
        '91125426'
    ])
);
