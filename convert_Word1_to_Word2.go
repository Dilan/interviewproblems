// https://leetcode.com/problems/edit-distance/

// Given two words word1 and word2,
// find the minimum number of operations required to convert word1 to word2.

// You can Insert / Delete / Replace

// Input: word1 = "horse", word2 = "ros"
// Output: 3
// Explanation:
// horse -> rorse (replace 'h' with 'r')
// rorse -> rose (remove 'r')
// rose -> ros (remove 'e')

package main

import "fmt"

func Min(a, b int) int {
    if a < b { return a }
    return b
}

func match(w1, w2 string, i, j int, cache [][]int) int {

    if i == len(w1) { return len(w2) - j }
    if j == len(w2) { return len(w1) - i }

    if cache[i][j] != -1 { return cache[i][j] }

    if w1[i] == w2[j] {
        cache[i][j] = match(w1, w2, i+1, j+1, cache);
    } else {

        del := match(w1, w2, i+1, j, cache);        // delete
        replace := match(w1, w2, i+1, j+1, cache);  // replace
        ins := match(w1, w2, i, j+1, cache);        // insert

        cache[i][j] = Min(del, Min(replace, ins)) + 1
    }

    return cache[i][j]

}

func minDistance(word1 string, word2 string) int {

    cache := make([][]int, len(word1))

    for i:= 0; i< len(word1); i++ {
        cache[i] = make([]int, len(word2))
        for j:= 0; j< len(word2); j++ {
            cache[i][j] = -1
        }
    }
    return match(word1, word2, 0, 0, cache)
}

func main() {

	res := minDistance("horse", "ros")
	fmt.Println("horse --> ros require", res, "operations")

}
