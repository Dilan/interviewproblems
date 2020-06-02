// https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

// You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only.
// Your task is to make these two strings equal to each other.
// You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

// Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

// Input: s1 = "xy", s2 = "yx"
// Output: 2
// Explanation:
// Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
// Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
// Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.

package main

import "fmt"

func minimumSwap(s1 string, s2 string) int {

    size := len(s1)
    x1 := make([]byte, 0, size)
    y1 := make([]byte, 0, size)
    x2 := make([]byte, 0, size)
    y2 := make([]byte, 0, size)

    for i := 0; i < len(s1); i ++ {
        if s1[i] != s2[i] {
            if string(s1[i]) == "x" {
                x1 = append(x1, s1[i])
                y2 = append(y2, s2[i])
            } else {
                y1 = append(y1, s1[i])
                x2 = append(x2, s2[i])
            }
        }
    }
    if (len(x1) + len(x2)) % 2 != 0 { return -1 }
    if (len(y1) + len(y2)) % 2 != 0 { return -1 }

    counter := len(x1) >> 1
    counter += len(y1) >> 1
    if len(x1) % 2 == 1 { counter += 2 }

    return counter
}

func main() {

	res := minimumSwap("xy", "yx")
	fmt.Println("Answer should be 2 -", res)

	res = minimumSwap("xxyyxyxyxx", "xyyxyxxxyx")
	fmt.Println("Answer should be 4 -", res)
}
