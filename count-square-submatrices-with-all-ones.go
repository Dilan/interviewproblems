// https://leetcode.com/problems/count-square-submatrices-with-all-ones/

// Count Square Submatrices with All Ones
// Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

/*
Input: matrix =
	[
	  [0,1,1,1],
	  [1,1,1,1],
	  [0,1,1,1]
	]
Output: 15
Explanation:
	There are 10 squares of side 1.
	There are 4 squares of side 2.
	There is  1 square of side 3.
	Total number of squares = 10 + 4 + 1 = 15.
*/

package main
import "fmt"

// https://leetcode.com/problems/count-square-submatrices-with-all-ones/

// Count Square Submatrices with All Ones
// Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

/*
Input: matrix =
	[
	  [0,1,1,1],
	  [1,1,1,1],
	  [0,1,1,1]
	]
Output: 15
Explanation:
	There are 10 squares of side 1.
	There are 4 squares of side 2.
	There is  1 square of side 3.
	Total number of squares = 10 + 4 + 1 = 15.
*/

package main
import "fmt"

func sum(input []int) int {
    sum := 0
    for i := range input {
        sum += input[i]
    }
    return sum
}

func MinOf(vars ...int) int {
    min := vars[0]
    for _, i := range vars {
        if min > i {
            min = i
        }
    }
    return min
}

func countSquares(matrix [][]int) int {

    var col_size, row_size int = len(matrix), len(matrix[0])

	s := make([][]int, len(matrix))
    for i := range s {
        s[i] = append(matrix[i][:0:0], matrix[i]...)
    }

    neighbors := [][]int{{1,0},{0,1}, {1,1}}

    for j := 0; j < col_size; j++ {
        for i := 0; i < row_size; i++ {
            if (matrix[j][i] == 0) { continue; }

            sn := make([]int,0,3) // slice length 0, capacity 3

            for n := 0; n < 3; n++ {
                y := neighbors[n][0] + j;
                x := neighbors[n][1] + i;

                if (x >= row_size || y >= col_size || matrix[y][x] == 0) {
                    break
                }
                sn = append(sn, s[y][x])
            }

            if (len(sn) == 3) {
                s[j+1][i+1] = 1 + MinOf(s[j][i], sn[0], sn[1])
            }
        }
    }

    answer := 0
    for i := range s {
        answer += sum(s[i])
    }
    return answer
}
