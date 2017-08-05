/**
 * A Stack machine is a simple system that performs arithmetic operations
 * on an input string of numbers and operators. It contains a stack that
 * can store an arbitrary number of 12-bit unsigned integers. Initially the
 * stack is empty. The machine processes a string of characters in the
 * following way:
 *
 * - the characters of the string are processed one by one;
 * - if the current character is a digit ('0'-'9'), the machine
 * pushes the value of that digit onto its stack;
 * - if the current character is '+', the machine pops the two
 * topmost values from its stack, adds them and pushes the result
 * onto the stack;
 * - if the current character is '*', the machine pops the two
 * topmost values from its stack, multiplies them and pushes the
 * result onto the stack;
 * - after the machine has processed the whole string it returns the
 * topmost value of its stack as the result;
 * - the machine reports an error if any operation it performs
 * (addition or multiplication) results in an overflow;<br/>
 * - the machine reports an error if it tries to pop an element from
 * its stack when the stack is empty, or if the stack is empty
 * after the machine has processed the whole string.
 *
 * For example, given the string "13+62*7+*" the machine will perform the
 * following operations:
*/

function Stack() {
    this.list = [];
    this.push = function(item) {
        this.list = [item].concat(this.list);
    };
        
    this.pop = function() {
        if (this.list.length == 0) {
            return undefined;
        }
        first = this.list[0];
        this.list = this.list.slice(1)
        return first
    }
    
    this.pick = function() {
        return this.list[0]
    }
}

var solution = function(str) {
    var commands = str.split(' ');
    var stack = new Stack();
    
    for(var i=0; i < commands.length; i++) {
        var cmd = commands[i];

        switch (cmd) {
            case '+':
                var num1 = stack.pop();
                var num2 = stack.pop();
                if (isNaN(num1) || isNaN(num2)) {
                    throw Error('should be two numbers in stack.');
                }
                stack.push(num1 + num2);
                break;
            case '-':
                var num1 = stack.pop();
                var num2 = stack.pop();
                if (isNaN(num1) || isNaN(num2)) {
                    throw Error('should be two numbers in stack.');
                }
                stack.push(num1 - num2);
                break;
            case 'POP':
                var num = stack.pop();
                break;
            case 'DUP':
                var num = stack.pick();
                if (isNaN(num)) {
                    throw Error('stack is empty.');
                }
                stack.push(num);
                break;
            default:
                var num = parseInt(cmd);
                if (isNaN(num) == false) {
                    stack.push(num);
                }
        }
    }
    return stack.pick();
};

var args = process.argv.slice(2);

try {
    var answer = solution(args[0]);
    console.log('Answer:', answer);
} catch(err) {
    console.log('Error:', err.message);
}
