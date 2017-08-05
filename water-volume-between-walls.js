/**
 http://qandwhat.apps.runkite.com/i-failed-a-twitter-interview/

                             ______
                            | 7  7 |___
         ___                |        6 |
        | 5 |˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜|          |
        |   |        ___| 4            |
     ___|   |    ___| 3                |
    | 2     |___| 2                    |
    |         1                        |
    ---------------------------------------->
*/
(function(land) {

    var leftMax = 0;
    var rightMax = 0;
    var left = 0;
    var right = land.length - 1;
    var volume = 0;

    while(left < right) {
        if(land[left] > leftMax) {
            leftMax = land[left];
        }
        if(land[right] > rightMax) {
            rightMax = land[right];
        }
        if(leftMax >= rightMax) {
            volume += rightMax - land[right];
            right--;
        } else {
            volume += leftMax - land[left];
            left++;
        }
    }

    console.log(volume);

})([2,5,1,2,3,4,7,7,6]);