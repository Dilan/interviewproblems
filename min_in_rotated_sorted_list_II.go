// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/

// Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
// (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
// (i.e., 3 3 1 3 might become 1 3 3 3).

// Find the minimum element.
// The array may contain duplicates

package main

import "fmt"

func findMin(arr []int) int {
    min := arr[0]
    queue := [][]int{{0, len(arr)-1 }}

    for i:=0; len(queue) > 0 ; i++ {
        ldx, rdx := queue[0][0], queue[0][1]
        queue = queue[1:] // pop 1st
        middle := ldx + (rdx - ldx) / 2

        if rdx == (ldx + 1) {
            if arr[ldx] < arr[rdx] && min > arr[ldx] {
                min = arr[ldx]
            } else if min > arr[rdx] {
                min = arr[rdx]
            }
            continue
        }

        if (arr[middle] <= arr[ldx]) && (ldx != middle) {
            queue = append(queue, []int{ldx,middle}) // choose left part
        }
        if (arr[middle] >= arr[rdx]) && (middle != rdx) {
            queue = append(queue, []int{middle, rdx}) // choose right part
        }
    }
    return min
}

func main() {
    fmt.Println(findMin([]int{1}) == 1)
    fmt.Println(findMin([]int{1,2}) == 1)
    fmt.Println(findMin([]int{2,1}) == 1)
    fmt.Println(findMin([]int{1,2,0}) == 0)
    fmt.Println(findMin([]int{4,5,6,7,1,2}) == 1)
    fmt.Println(findMin([]int{4,5,6,7,8,9,0,1,2}) == 0)
    fmt.Println(findMin([]int{1,2,3,4,5,6,7,8,9}) == 1)
    fmt.Println(findMin([]int{3,3,1,3}) == 1)
    fmt.Println(findMin([]int{3,3,1,3,3,3}) == 1)
    fmt.Println(findMin([]int{1,3,3,3,3,4}) == 1)
}
