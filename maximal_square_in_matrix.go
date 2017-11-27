/*
    Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
    For example, given the following matrix:

    1  0  1  0  0
    1  0 |1``1| 1
    1  1 |1..1| 1
    1  0  0  1  0

    return 4
*/

package main

import (
    "fmt"
)

func minNeighborSize(i, j int, matrix [][]int) int {
    if i == 0 || j == 0 {
        return 0
    } else {
        min := matrix[i-1][j-1]
        if matrix[i][j-1] < min {
            min = matrix[i][j-1]
        }
        if matrix[i-1][j] < min {
            min = matrix[i-1][j]
        }
        return min
    }
}

func maximalSquare(matrix [][]byte) int {
    dp := make([][]int, len(matrix))
    for i := range(matrix) {
        dp[i] = make([]int, len(matrix[i]))
    }

    maxSize := 0
    for i := range(matrix) {
        for j := range(matrix[i]) {
            if string(matrix[i][j]) == "0" {
                dp[i][j] = 0
            } else {
                dp[i][j] = 1 + minNeighborSize(i, j, dp)
                if dp[i][j] > maxSize {
                    maxSize = dp[i][j]
                }
            }
        }
    }
    return maxSize * maxSize
}

func main()  {
    m1 := [][]byte {
        {'1','0','1','0','0'},
        {'1','0','1','1','1'},
        {'1','1','1','1','1'},
        {'1','0','0','1','0'},
    }
    fmt.Println(maximalSquare(m1))

    m2 := [][]byte{
        []byte("1011"),
        []byte("1011"),
    }
    fmt.Println(maximalSquare(m2))

    m3 := [][]byte{
        {48,48,49,49},
        {48,48,49,49},
    }
    fmt.Println(maximalSquare(m3))
}
