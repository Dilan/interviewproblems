var solution = function(list) {
    var merge = function(item, list) {
        var result = [item];
        for(var i=0; i<list.length; i++) {
            // overlap
            if (result[0][0] <= list[i][1] && list[i][0] <= result[0][1]) {
                result[0][0] = Math.min(result[0][0], list[i][0]);
                result[0][1] = Math.max(result[0][1], list[i][1]);
            } else {
                result.push(list[i]);
            }
        }
        return result;
    };

    var result = [list[0]];
    list.slice(1).forEach(function(item) {
        result = merge(item, result)
    });

    return result.sort(function(a,b) {
        return a[0] > b[0]
    });
};

console.log(
    solution([[10,11], [0,2], [3,5], [7,9], [12,19]])
);

console.log(
    solution([[0,8], [0,2], [3,5], [7,9], [11,13]])
);

console.log(
    solution([[1,9], [1,8], [1,7], [5,6], [0,1]])
);

console.log(
    solution([[2,10], [2,9], [5,6], [12,14], [1,4]])
);

/*
 Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.

 To do this, you’ll need to know when any team is having a meeting. In HiCal, a meeting is stored as an object of a Meeting class with integer variables startTime andendTime. These integers represent the number of 30-minute blocks past 9:00am.

 public class Meeting {

 int startTime;
 int endTime;

 public Meeting(int startTime, int endTime) {
 // number of 30 min blocks past 9:00 am
 this.startTime = startTime;
 this.endTime   = endTime;
 }

 public String toString() {
 return String.format("(%d, %d)", startTime, endTime);
 }
 }

 Java

 For example:

 new Meeting(2, 3); // meeting from 10:00 – 10:30 am
 new Meeting(6, 9); // meeting from 12:00 – 1:30 pm

 Write a function condenseMeetingTimes() that takes a list of meeting time ranges and returns a list of condensed ranges.

 For example, given:

 [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

 your function would return:

 [(0, 1), (3, 8), (9, 12)]

 Do not assume the meetings are in order. The meeting times are coming from multiple teams.

 In this case the possibilities for startTime and endTime are bounded by the number of 30-minute slots in a day. But soon you plan to refactor HiCal to store times as Unix timestamps (which are big numbers).Write something that's efficient even when we can't put a nice upper bound on the numbers representing our time ranges.

 */