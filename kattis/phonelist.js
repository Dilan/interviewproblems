/*
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

var list = [
    '113',
    '12340',
    '123440',
    '12345',
    '98346',
];

var hm = {};

list.forEach((phone) => {
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
            console.log('error :: [not consistent]');
            process.exit(1);
        } else {
            root = root[n];
        }
    }
});

console.log('Done :: [consistent]');
