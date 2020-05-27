// https://leetcode.com/problems/contiguous-array/

// Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
// Input: [0,1,0]
// Output: 2
// Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

import "fmt"

func Max (x, y int) int {
    if x > y {
        return x
    }
    return y
}

func findMaxLength(nums []int) int {
    hm := make(map[int]int)
    var count, length, maxLength int;

    for i := 0; i < len(nums); i++ {
        if nums[i] == 1 {
            count += 1
        } else {
            count -= 1
        }

        _, ok := hm[count]
        if ok == false {
            hm[count] = i
        }

        if count == 0 {
            length = i + 1
        } else {
            length = i - hm[count]
        }

        maxLength = Max(maxLength, length)
    }
    return maxLength
}
