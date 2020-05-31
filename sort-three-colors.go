// https://leetcode.com/problems/sort-colors/
//
// Given an array with n objects colored red, white or blue, sort them in-place so
// that objects of the same color are adjacent, with the colors in the order red, white and blue.
//
// Input: [2,0,2,1,1,0]
// Output: [0,0,1,1,2,2]

package main
import "fmt"

func sortColors(nums []int)  {
    var start, end int = 0, len(nums)-1
    for i := 0; i <= end; {
        if nums[i] == 0 {
            nums[start], nums[i] = 0, nums[start]
            start += 1
            i += 1
        } else if nums[i] == 2 {
            nums[end], nums[i] = 2, nums[end]
            end -= 1
        } else {
            i += 1
        }
    }
}

func main() {
    input := []int{2,0,2,1,1,0}
    fmt.Println("Before", input)
    sortColors(input)
    fmt.Println("After ", input)
}
