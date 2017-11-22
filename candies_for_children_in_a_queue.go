/*
    There are N children standing in a line. Each child is assigned a rating value.
    You are giving candies to these children subjected to the following requirements:
    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.
    What is the minimum candies you must give?
*/
package main

import (
    "fmt"
)

func candy(ratings []int) int {
    candyList := make([]int, len(ratings))

    candyList[0] = 1
    for i := 1; i < len(ratings); i++ {
        if ratings[i] > ratings[i-1] {
            candyList[i] = candyList[i-1] + 1
        } else {
            candyList[i] = 1
        }
    }
    // check from right to left (correction)
    for i := len(ratings)-2; i >= 0; i-- {
        if ratings[i] > ratings[i+1] && candyList[i] <= candyList[i+1] {
            candyList[i] = candyList[i+1] + 1
        }
    }
    result := 0
    for _, amount := range(candyList) {
        result += amount
    }
    return result
}

func main() {
    fmt.Println(candy([]int{8,9,0,7,0,7,2,1}))
    fmt.Println(candy([]int{5,3,1}))
    fmt.Println(candy([]int{1,2,5,3}))
}
