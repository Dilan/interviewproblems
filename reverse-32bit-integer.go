// https://leetcode.com/problems/reverse-integer/
// Given a 32-bit signed integer, reverse digits of an integer.


import (
    "strconv"
    "strings"
    "math"
    "fmt"
)

func reverse(x int) int {
    coff := 1
    if x < 0 {
        coff = -1
    }
    
    s := strconv.Itoa(x * coff)
    r := []rune(s)
    l := len(s)
    
    
    for i := 0; i < (l / 2); i++ {
        r[i], r[l-i-1] = r[l-i-1], r[i]   
    }
    
    i, _ := strconv.Atoi(string(r))
    
    if float64(i) > math.Pow(2, float64(31)) {
        return 0
    }
    
    return i * coff
}