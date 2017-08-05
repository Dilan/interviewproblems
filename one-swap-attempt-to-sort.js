/**
    Given an array with n elements, 
    Question: can we sort this array in ascending order by performing only one (or less) swap operation?
*/
function solution(A) {
    var list = A.slice(0); // copy
    var attemptsLimit = arguments[1] || 1;
    
    console.log(list);
    
    var prevItem = list[0];
    var prevItemIndex = 0;
    var swappedValue;
    var swapCounter = 0;
    var idx = 1;
    
    while (idx < list.length && attemptsLimit >= 0) {
        var item = list[idx];
        
        if (item > prevItem) {
            prevItem = item;
            prevItemIndex = idx;
        }
        else if (item < prevItem) {
            if (swappedValue != item) {
                swapCounter++;
                attemptsLimit--;
                swappedValue = item;
            }
            list[prevItemIndex] = item;
            list[idx] = prevItem;
        }
        
        idx++;
        
        // start again
        if (idx == list.length && swapCounter > 0) {
            swappedValue = undefined;
            var prevItem = list[0];
            var prevItemIndex = 0;
            idx = 1;
            swapCounter = 0;
        }
    }
    return (attemptsLimit >=0);
}

// console.log(solution([1, 5, 3, 3, 7]))
// console.log(solution([1,3,4]))
// console.log(solution([4,3,2]))
// console.log(solution([1,5,7,2]))
console.log(solution([2, 3, 4, 5, 6, 7, 8, 1]));
