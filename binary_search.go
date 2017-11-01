package main

import (
    "fmt"
)

func binarySearch(arr []int, num int) int {
    var middle int;
    ldx := 0
    rdx := len(arr)

    for i := 0; ; i++ {
        middle = ldx + (rdx - ldx) / 2

        if num == arr[middle] {
            return middle
        } else if ldx >= rdx {
            break
        } else if num > arr[middle] {
            ldx = middle // right ---> |
        } else {
            rdx = middle // left | <---
        }
    }
    return -1
}

func main() {
    arr := []int{1,2,3,4,6,8,12,13,18,19}

    num := 18
    idx := binarySearch(arr, num)

    fmt.Println("answer:",idx, arr[idx], "==", num)



}
