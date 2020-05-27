// https://leetcode.com/problems/possible-bipartition/

// Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
// Example 1:

// Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
// Output: true
// Explanation: group1 [1,4], group2 [2,3]

package main

import "fmt"

func possibleBipartition(N int, dislikes [][]int) bool {

    graph := make(map[int]map[int]bool)
    for i := 1; i <= N; i++ {
        graph[i] = make(map[int]bool)
    }

    for _, tuple := range(dislikes) {
        a := tuple[0]
        b := tuple[1]
        graph[a][b] = true
        graph[b][a] = true
    }

    g1 := 1

    var n int
    queue := make([]int, 0, N)
    groups := make(map[int]int)

    for i := 1; i <= N; i++ {
        _, exist := groups[i]
        if exist { continue }

        queue = append(queue, i)
        groups[i] = g1

        for ; len(queue) > 0; {
            n, queue = queue[len(queue)-1], queue[:len(queue)-1]

            for nn := range(graph[n]) {
                _, exist := groups[nn]
                if exist == false {
                    queue = append(queue, nn)
                    groups[nn] = groups[n] * -1
                    continue
                }
                if (groups[nn] == groups[n]) {
                    return false
                }
            }

        }
    }

    return true
}

func main() {

	f := possibleBipartition(
		4,
		[][]int{
			{1,2},
			{1,3},
			{2,4}})
	fmt.Println(f)
}
