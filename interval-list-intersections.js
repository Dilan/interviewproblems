/*
https://leetcode.com/problems/interval-list-intersections/

Given two lists of closed intervals, each list of intervals is pairwise disjoint
and in sorted order.
Return the intersection of these two interval lists.

Example:
        Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
        Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

                A  [--]    [-----]        [-----------]    [-]
                B   [------]    [-----]      [------------]   [-]
answer      [--]   []   [--]         [--------]   [] []

*/
var compare = (a, b) => {

    var intersection;
    let [x1, y1] = a
    let [x2, y2] = b

    if (y1 <= x2 || y2 <= x1) { // no intersection

        if (y2 > y1) {      // (b) is longer
            a = null;
            intersection = (x2 == y1) ? [y1, x2] : null;

        } else {            // (a) is longer
            b = null;
            intersection = (x1 == y2) ? [y2, x1] : null;
        }

    } else {
        intersection = [Math.max(x1, x2), Math.min(y1, y2)]

        if (y2 > y1) {      // (b) is longer
            a = null
            b = [intersection[1], y2]

        } else {            // (a) is longer
            b = null
            a = [intersection[1], y1]
        }
    }
    return [intersection, a, b]
}

/**
 * @param {number[][]} A
 * @param {number[][]} B
 * @return {number[][]}
 */
var intervalIntersection = function(A, B) {

    var result = [];
    var a = A.shift();
    var b = B.shift();

    while(a && b) {
        var [insec, a, b] = compare(a, b)

        if (insec) result.push(insec);
        if (a == null) a = A.shift()
        if (b == null) b = B.shift()
    }
    return result

};
