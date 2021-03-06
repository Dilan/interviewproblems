// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/

// Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
// (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
// (i.e., 3 3 1 3 might become 1 3 3 3).

// Find the minimum element.
// The array (may) contain duplicates

package main

import "fmt"

func findMin(nums []int) int {
    min := nums[0];
    for _, val := range(nums[1:]) {
        if val == min {
            continue
        }
        if val < min {
            min = val
            break
        }
    }
    return min
}

func main() {
    fmt.Println(findMin([]int{1,2,0}))
    fmt.Println(findMin([]int{4,5,6,7,1,2}))
    fmt.Println(findMin([]int{3,3,1,3}))
}
