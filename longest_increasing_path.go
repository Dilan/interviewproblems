package main

import (
    "fmt"
)

type Point struct {
    X, Y int
}

func neighbors(point Point, matrix [][]int) []Point {
    conditions := [][]int{{-1,0},{1,0},{0,-1},{0,1}}
    result := []Point{}
    for _, p := range(conditions) {
        i, j := (point.X + p[0]), (point.Y + p[1])
        if (i >= 0 && i < len(matrix)) && (j >= 0 && j < len(matrix[i]) && matrix[i][j] > matrix[point.X][point.Y]) {
            result = append(result, Point{i,j})
        }
    }
    return result
}

func dfs(p *Point, matrix [][]int, visited map[Point][]Point) []Point {
    path, isVisited := visited[*p]
    if isVisited {
        return path
    }

    longestPath := []Point{}
    for _, n := range(neighbors(*p, matrix)) {
        path := dfs(&n, matrix, visited)
        if len(path) > len(longestPath) {
            longestPath = path
        }
    }
    visited[*p] = append(longestPath, *p) // cache

    return visited[*p]
}


func longestIncreasingPath(matrix [][]int) int {
    visited := make(map[Point][]Point)
    for i, _ := range(matrix) {
        for j, _ := range(matrix[i]) {
            dfs(&Point{i,j}, matrix, visited)
        }
    }

    max := 0
    for _, lp := range(visited) {
        if max < len(lp) {
            max = len(lp)
        }
    }
    return max
}

func main()  {
    p0 := longestIncreasingPath([][]int{
        { 9,9,4 },
        { 6,6,8 },
        { 2,1,1 },
    })
    p1 := longestIncreasingPath([][]int{
        { 1,2 },
        { 3,7 },
        { 4,5 },
    })

    fmt.Println(p0)
    fmt.Println(p1)
}
